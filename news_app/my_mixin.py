from .models import Viewer


class CountViewMixin:

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip



    # def perform_count_view(self, instance, request):
    #     viewer, created = Viewer.objects.get_or_create(
    #         ipaddress=request.META['REMOTE_ADDR'],
    #     )
    #     if instance.viewers.filter(id=viewer.id).count() == 0:
    #         instance.viewers.add(viewer)



    # def perform_count_view(self, request, *args, **kwargs):
    #     response = super().retrieve(request, *args, **kwargs)
    #     if hasattr(response, 'viewers'):
    #         viewer, created = Viewer.objects.get_or_create(
    #             ip_address=request.META['REMOTE_ADDR'],
    #         )
    #         if self.object.viewers.filter(id=viewer.id).count() == 0:
    #             self.object.viewers.add(viewer)

        # return response


