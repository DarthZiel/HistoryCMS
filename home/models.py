from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel,MultiFieldPanel,InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from django.db import models
from wagtail.core.fields import RichTextField, StreamField
from wagtail.models import Page, Orderable
from wagtail.core.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from modelcluster.fields import ParentalKey


from .blocks import NewBlock
class HomePageCarouselImages(Orderable):
    """Between 1 and 5 images for the home page carousel."""

    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [ImageChooserPanel("carousel_image")]

class HomePage(Page):
    article = models.TextField(default='контент',blank=True)
    # rtfbody = RichTextField(null=True, blank=True)
    # img = models.ForeignKey(
    #     'wagtailimages.Image',
    #     blank=True,
    #     null= True,
    #     on_delete= models.SET_NULL,
    # )
    body = StreamField([
        ('newblock', NewBlock()),
        ],
        blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('article'),
        StreamFieldPanel('body'),
        MultiFieldPanel(
            [InlinePanel("carousel_images", max_num=5, min_num=1, label="Image")],
            heading="Carousel Images",
        ),
    ]

