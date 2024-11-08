from typing import Any


class CommandMixin:
    title: str = None

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super(CommandMixin, self).get_context_data(**kwargs)
        context["title"] = self.title
        return context
