# Generated by Django 3.1.2 on 2020-11-24 11:46

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.blocks.field_block
import wagtail.core.fields
import wagtail.images.blocks
import wagtailnhsukfrontend.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0025_auto_20201124_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basepage',
            name='body',
            field=wagtail.core.fields.StreamField([('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('new_window', wagtail.core.blocks.BooleanBlock(label='Open in new window', required=False))], group='Base')), ('care_card', wagtail.core.blocks.StructBlock([('type', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Non-urgent'), ('urgent', 'Urgent'), ('immediate', 'Immediate')])), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.StreamBlock([('richtext', wagtail.core.blocks.RichTextBlock()), ('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('new_window', wagtail.core.blocks.BooleanBlock(label='Open in new window', required=False))])), ('details', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.StreamBlock([('richtext', wagtail.core.blocks.RichTextBlock()), ('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('new_window', wagtail.core.blocks.BooleanBlock(label='Open in new window', required=False))])), ('inset_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('warning_callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('summary_list', wagtail.core.blocks.StructBlock([('rows', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.SummaryListRowBlock)), ('no_border', wagtail.core.blocks.BooleanBlock(default=False, required=False))]))], required=True))])), ('inset_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('grey_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(label='heading', required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no heading. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('warning_callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('summary_list', wagtail.core.blocks.StructBlock([('rows', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.SummaryListRowBlock)), ('no_border', wagtail.core.blocks.BooleanBlock(default=False, required=False))]))], required=True))], group='Base')), ('details', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.StreamBlock([('richtext', wagtail.core.blocks.RichTextBlock()), ('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('new_window', wagtail.core.blocks.BooleanBlock(label='Open in new window', required=False))])), ('inset_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('warning_callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('summary_list', wagtail.core.blocks.StructBlock([('rows', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.SummaryListRowBlock)), ('no_border', wagtail.core.blocks.BooleanBlock(default=False, required=False))]))], required=True))], group='Base')), ('do_list', wagtail.core.blocks.StructBlock([('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('label', wagtail.core.blocks.CharBlock(help_text='Adding a label here will overwrite the default of Do', label='Heading', required=False)), ('do', wagtail.core.blocks.ListBlock(wagtail.core.blocks.field_block.RichTextBlock))], group='Base')), ('dont_list', wagtail.core.blocks.StructBlock([('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('label', wagtail.core.blocks.CharBlock(help_text="Adding a label here will overwrite the default of Don't", label='Heading', required=False)), ('dont', wagtail.core.blocks.ListBlock(wagtail.core.blocks.field_block.RichTextBlock))], group='Base')), ('expander', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.StreamBlock([('richtext', wagtail.core.blocks.RichTextBlock()), ('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('new_window', wagtail.core.blocks.BooleanBlock(label='Open in new window', required=False))])), ('inset_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('grey_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(label='heading', required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no heading. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('warning_callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('summary_list', wagtail.core.blocks.StructBlock([('rows', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.SummaryListRowBlock)), ('no_border', wagtail.core.blocks.BooleanBlock(default=False, required=False))]))], required=True))], group='Base')), ('expander_group', wagtail.core.blocks.StructBlock([('expanders', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.ExpanderBlock))], group='Base')), ('inset_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True))], group='Base')), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))], group='Base')), ('panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))], group='Base')), ('panel_list', wagtail.core.blocks.StructBlock([('panels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('left_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('right_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))]))])))], group='Base')), ('grey_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(label='heading', required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no heading. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))], group='Base')), ('warning_callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))], group='Base')), ('summary_list', wagtail.core.blocks.StructBlock([('rows', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.SummaryListRowBlock)), ('no_border', wagtail.core.blocks.BooleanBlock(default=False, required=False))], group='Base')), ('promo', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('heading', wagtail.core.blocks.CharBlock(required=True)), ('description', wagtail.core.blocks.CharBlock(required=False)), ('content_image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small')], required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2))], group='Base')), ('promo_group', wagtail.core.blocks.StructBlock([('column', wagtail.core.blocks.ChoiceBlock(choices=[('one-half', 'One-half'), ('one-third', 'One-third')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small')], required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('promos', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.BasePromoBlock))], group='Base')), ('recent_posts', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock())], group='Custom'))], blank=True),
        ),
        migrations.AlterField(
            model_name='componentspage',
            name='body',
            field=wagtail.core.fields.StreamField([('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('new_window', wagtail.core.blocks.BooleanBlock(label='Open in new window', required=False))], group='Base')), ('care_card', wagtail.core.blocks.StructBlock([('type', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Non-urgent'), ('urgent', 'Urgent'), ('immediate', 'Immediate')])), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.StreamBlock([('richtext', wagtail.core.blocks.RichTextBlock()), ('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('new_window', wagtail.core.blocks.BooleanBlock(label='Open in new window', required=False))])), ('details', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.StreamBlock([('richtext', wagtail.core.blocks.RichTextBlock()), ('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('new_window', wagtail.core.blocks.BooleanBlock(label='Open in new window', required=False))])), ('inset_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('warning_callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('summary_list', wagtail.core.blocks.StructBlock([('rows', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.SummaryListRowBlock)), ('no_border', wagtail.core.blocks.BooleanBlock(default=False, required=False))]))], required=True))])), ('inset_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('grey_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(label='heading', required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no heading. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('warning_callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('summary_list', wagtail.core.blocks.StructBlock([('rows', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.SummaryListRowBlock)), ('no_border', wagtail.core.blocks.BooleanBlock(default=False, required=False))]))], required=True))], group='Base')), ('details', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.StreamBlock([('richtext', wagtail.core.blocks.RichTextBlock()), ('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('new_window', wagtail.core.blocks.BooleanBlock(label='Open in new window', required=False))])), ('inset_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('warning_callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('summary_list', wagtail.core.blocks.StructBlock([('rows', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.SummaryListRowBlock)), ('no_border', wagtail.core.blocks.BooleanBlock(default=False, required=False))]))], required=True))], group='Base')), ('do_list', wagtail.core.blocks.StructBlock([('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('label', wagtail.core.blocks.CharBlock(help_text='Adding a label here will overwrite the default of Do', label='Heading', required=False)), ('do', wagtail.core.blocks.ListBlock(wagtail.core.blocks.field_block.RichTextBlock))], group='Base')), ('dont_list', wagtail.core.blocks.StructBlock([('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('label', wagtail.core.blocks.CharBlock(help_text="Adding a label here will overwrite the default of Don't", label='Heading', required=False)), ('dont', wagtail.core.blocks.ListBlock(wagtail.core.blocks.field_block.RichTextBlock))], group='Base')), ('expander', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.StreamBlock([('richtext', wagtail.core.blocks.RichTextBlock()), ('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('new_window', wagtail.core.blocks.BooleanBlock(label='Open in new window', required=False))])), ('inset_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('grey_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(label='heading', required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no heading. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('warning_callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('summary_list', wagtail.core.blocks.StructBlock([('rows', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.SummaryListRowBlock)), ('no_border', wagtail.core.blocks.BooleanBlock(default=False, required=False))]))], required=True))], group='Base')), ('expander_group', wagtail.core.blocks.StructBlock([('expanders', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.ExpanderBlock))], group='Base')), ('inset_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True))], group='Base')), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))], group='Base')), ('panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))], group='Base')), ('panel_list', wagtail.core.blocks.StructBlock([('panels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('left_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('right_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))]))])))], group='Base')), ('grey_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(label='heading', required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no heading. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))], group='Base')), ('warning_callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))], group='Base')), ('summary_list', wagtail.core.blocks.StructBlock([('rows', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.SummaryListRowBlock)), ('no_border', wagtail.core.blocks.BooleanBlock(default=False, required=False))], group='Base')), ('promo', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('heading', wagtail.core.blocks.CharBlock(required=True)), ('description', wagtail.core.blocks.CharBlock(required=False)), ('content_image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small')], required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2))], group='Base')), ('promo_group', wagtail.core.blocks.StructBlock([('column', wagtail.core.blocks.ChoiceBlock(choices=[('one-half', 'One-half'), ('one-third', 'One-third')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small')], required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=6, min_value=2)), ('promos', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.BasePromoBlock))], group='Base')), ('recent_posts', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock())], group='Custom'))], blank=True),
        ),
    ]
