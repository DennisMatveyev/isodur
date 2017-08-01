# from django.core.urlresolvers import reverse
# from .models import Section, Project
#
#
# # Product
#
#
# def sections_processor(request):
#     sections = Section.objects.filter(visible=True)
#     urls = {
#         "company": reverse('company'),
#         "contacts": reverse('contacts'),
#         "projects": {
#             "url": reverse('project_list'),
#             "fields": [{"url": reverse('project_detail', kwargs={"slug": item.slug}),
#                         "title": item.title} for item in Project.objects.all()]
#         },
#         # "partners": reverse('partners'),
#         # "advantages": reverse('advantages'),
#         # "products": {
#         #     "url": reverse('product_list'),
#         #     "fields": [{"url": reverse('product_detail', kwargs={"slug": item.slug}),
#         #                 "title": item.name} for item in Product.objects.all()]
#         # },
#     }
#     return {'urls': urls.items(),
#             "sections": sections}
