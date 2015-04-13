from django.contrib import admin
from app.note.models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'user')
    # list_filter = ('pub_date',)
    search_fields = ('title', 'body')
    readonly_fields = ('user',)

    fieldsets = [
        ('', {'fields': ['title', 'body', 'user']}),
        ('Date Information', {'fields': ['pub_date']})
    ]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()


# Register your models here.

admin.site.register(Note, NoteAdmin)
