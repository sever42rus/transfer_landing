from django.shortcuts import get_object_or_404, render
from django.views.generic import View
from rest_framework.generics import ListAPIView

from .forms import RecallForm
from .models import Recall, RecallInvite
from .serializers import RecallListSerializer
from .services import PaginationReview

# Create your views here.


class RecallListAPI(ListAPIView):

    serializer_class = RecallListSerializer
    pagination_class = PaginationReview
    queryset = Recall.objects.filter(
        verified=True).order_by('-datetime_create')[:20]


class RecallInviteAdd(View):

    templates = 'recall/form.html'
    templates_done = 'recall/done.html'

    def get(self, request, invite_id):
        recal_invite = get_object_or_404(RecallInvite, id=invite_id)
        if recal_invite.done:
            return render(request, self.templates_done, {'recal_invite': recal_invite, })
        recall_form = RecallForm()
        return render(request, self.templates, {'recal_invite': recal_invite, 'recall_form': recall_form})

    def post(self, request, invite_id):
        recal_invite = RecallInvite.objects.filter(id=invite_id).first()
        if recal_invite.done:
            return render(request, self.templates_done, {'recal_invite': recal_invite, })
        recall_form = RecallForm(request.POST)
        if recall_form.is_valid():
            new_recall = recall_form.save(commit=False)
            new_recall.feedback = recal_invite.feedback
            new_recall.save()
            recal_invite.done = True
            recal_invite.save()
            return render(request, self.templates_done, {'recal_invite': recal_invite, })

        return render(request, self.templates, {'recal_invite': recal_invite, 'recall_form': recall_form})
