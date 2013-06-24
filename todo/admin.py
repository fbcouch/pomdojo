from django.contrib import admin
from todo.models import Item, TodoList


class ItemInline(admin.TabularInline):
    model = Item
    extra = 1

    fields = ['finished', 'title', 'owner', 'due_on', 'due_at', 'priority']

class TodoListAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    
admin.site.register(TodoList, TodoListAdmin)
admin.site.register(Item)