"""Markdown utils."""

import json
import markdown as markdown_module
import nh3

from django.template import loader
from django.urls import reverse
from django.utils.encoding import force_str
from django.utils.safestring import mark_safe

from . import settings


MAX_MARKDOWN_LENGTH = 256 * 1024  # 256 KB


def markdown(
    value,
    extensions=settings.MARKDOWN_EXTENSIONS,
    extension_configs=settings.MARKDOWN_EXTENSION_CONFIGS,
    sanitize=True,
):
    """Render markdown over a given value, optionally using various extensions.

    Default extensions could be defined with MARKDOWN_EXTENSIONS option.

    HTML output is sanitized with nh3 by default. Pass sanitize=False only
    for trusted content.

    :returns: A rendered markdown

    """
    text = force_str(value)[:MAX_MARKDOWN_LENGTH]
    html = markdown_module.markdown(
        text, extensions=extensions, extension_configs=extension_configs
    )
    if sanitize:
        html = nh3.clean(html)
    return mark_safe(html)


def editor_js_initialization(selector, **extra_settings):
    """Return script tag with initialization code."""

    init_template = loader.get_template(settings.MARKDOWN_EDITOR_INIT_TEMPLATE)

    options = dict(
        previewParserPath=reverse("django_markdown_preview"),
        **settings.MARKDOWN_EDITOR_SETTINGS,
    )
    options.update(extra_settings)
    config = {"selector": selector, "extra_settings": options}
    ctx = dict(config_json=mark_safe(json.dumps(config)))
    return init_template.render(ctx)
