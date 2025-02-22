from django import forms
from django.contrib import admin

from .models import (
    Event,
    Officer,
    Officership,
    Person,
    Politburo,
    PolitburoMembership,
    Sponsor,
    Sponsorship,
    Semester,
    UcbClass,
)
from .constants import DAYS_OF_WEEK, OH_TIMES, OH_CHOICES


class OfficershipAdminForm(forms.ModelForm):
    office_hours = forms.CharField(widget=forms.Select(choices=OH_CHOICES))
    tutor_subjects = forms.ModelMultipleChoiceField(
        required=False, queryset=UcbClass.objects, widget=forms.CheckboxSelectMultiple
    )


class SponsorshipInline(admin.TabularInline):
    model = Sponsorship
    extra = 0


class OfficershipInline(admin.TabularInline):
    form = OfficershipAdminForm
    model = Officership
    extra = 0


class PolitburoMembershipInline(admin.TabularInline):
    model = PolitburoMembership
    extra = 0


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    inlines = [OfficershipInline, PolitburoMembershipInline, SponsorshipInline]


@admin.register(Officer)
class OfficerAdmin(admin.ModelAdmin):
    inlines = [OfficershipInline]


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(UcbClass)
class UcbClassAdmin(admin.ModelAdmin):
    pass


# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    actions = ["duplicate_events", "enable_events", "disable_events"]

    def disable_events(modeladmin, request, queryset):
        queryset.update(enabled=False)

    def enable_events(modeladmin, request, queryset):
        queryset.update(enabled=True)

    def duplicate_events(modeladmin, request, queryset):
        for event in queryset:
            event.pk = None
            event.save()


@admin.register(Politburo)
class PolituburoAdmin(admin.ModelAdmin):
    inlines = [PolitburoMembershipInline]


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    inlines = [SponsorshipInline]
