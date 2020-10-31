from django.http import HttpResponse
from django.views.generic import FormView, DetailView, ListView
import magic
from .exceptions import NotEvenPagination
from .forms import ImgUpload
from .models import Img


class ImgFormView(FormView):
    template_name = 'img/upload_form.html'
    form_class = ImgUpload
    success_url = '/'

    def form_valid(self, form):
        new_img = Img.objects.create(**form.cleaned_data)
        new_img.save()
        return super(ImgFormView, self).form_valid(form)


class ImgListView(ListView):
    paginate_by = 6
    queryset = Img.objects.filter(is_active=True)
    template_name = 'img/img_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        if self.paginate_by % 2 != 0:
            raise NotEvenPagination
        context = super(ImgListView, self).get_context_data()
        context['first_row'] = context['page_obj'][:len(context['page_obj'])//2]
        context['second_row'] = context['page_obj'][len(context['page_obj'])//2:]
        return context


class ImgDetail(DetailView):
    queryset = Img.objects.filter(is_active=True)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        f_type = magic.from_buffer(self.object.img.read(2048), mime=True)
        self.object.img.seek(0)
        return HttpResponse(self.object.img.read(), f_type)
