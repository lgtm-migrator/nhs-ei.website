# Generated by Django 3.2.13 on 2022-05-13 10:07

from django.db import migrations
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0005_auto_20220512_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='documents',
            field=wagtail.fields.StreamField([('document_group', wagtail.blocks.StreamBlock([('document', wagtail.blocks.StructBlock([('title', wagtail.blocks.RichTextBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('summary', wagtail.blocks.RichTextBlock(required=False))])), ('document_link', wagtail.blocks.StructBlock([('title', wagtail.blocks.RichTextBlock(required=False)), ('external_url', wagtail.blocks.URLBlock(required=False)), ('page', wagtail.blocks.PageChooserBlock(required=False)), ('summary', wagtail.blocks.RichTextBlock(required=False))])), ('document_embed', wagtail.blocks.StructBlock([('title', wagtail.blocks.RichTextBlock(required=False)), ('html', wagtail.blocks.RawHTMLBlock())])), ('free_text', wagtail.blocks.RichTextBlock())], group='Custom')), ('jump_menu', wagtail.blocks.StructBlock([('menu', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('menu_id', wagtail.blocks.CharBlock())])))], group='Custom')), ('named_anchor', wagtail.blocks.StructBlock([('anchor_id', wagtail.blocks.CharBlock()), ('heading', wagtail.blocks.CharBlock(required=False))], group='Custom'))], blank=True, use_json_field=True),
        ),
    ]
