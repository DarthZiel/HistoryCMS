
from wagtail.core.blocks import RichTextBlock,StructBlock, CharBlock
from wagtail.images.blocks import ImageChooserBlock


class NewBlock(StructBlock):
    title = CharBlock(blank=True)
    info = RichTextBlock()
    image = ImageChooserBlock()

    class Meta:
        template = 'blocks/new_block.html'
