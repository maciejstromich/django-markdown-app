"""Supports preview."""

from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from . import settings
from .utils import MAX_MARKDOWN_LENGTH


@csrf_protect
def preview(request):
    """Render preview page.

    :returns: A rendered preview

    """
    if settings.MARKDOWN_PROTECT_PREVIEW:
        user = getattr(request, "user", None)
        if not user or not user.is_staff:
            from django.contrib.auth.views import redirect_to_login

            return redirect_to_login(request.get_full_path())

    content = request.POST.get("data", "No content posted")
    if len(content) > MAX_MARKDOWN_LENGTH:
        return HttpResponseBadRequest("Content too large")

    return render(
        request,
        settings.MARKDOWN_PREVIEW_TEMPLATE,
        dict(
            content=content,
            css=settings.MARKDOWN_STYLE,
        ),
    )
