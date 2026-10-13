from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils.text import slugify


class ActivityLog(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    done_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                related_name="activity_logs")
    is_removed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Activity Log"
        verbose_name_plural = "Activity Logs"


class Status(models.Model):
    name = models.CharField(max_length=100)
    is_removed = models.BooleanField(default=False)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                 related_name="statuses_added")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

    def __str__(self):
        return self.name


class Clinic(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True, blank=True)
    # Upgraded to 6 decimal places for exact map pinpointing
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=0.000000, null=True, blank=True)
    long = models.DecimalField(max_digits=9, decimal_places=6, default=0.000000, null=True, blank=True)
    is_removed = models.BooleanField(default=False)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                 related_name="clinics_added")
    created_at = models.DateTimeField(auto_now_add=True),
    image_url =  models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    is_removed = models.BooleanField(default=False)
    # Fixed duplicate related_name string conflict here
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                 related_name="categories_added")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    examples = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Treatment(models.Model):
    # Core Information
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True, help_text="URL-friendly identifier")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True,
                                 related_name="treatments")
    description = models.TextField(blank=True, null=True, help_text="Detailed description of the procedure.")

    # Financials (CAD)
    base_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0.00)],
        help_text="Standard cost per single session (CAD)."
    )
    package_price_3_sessions = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Discounted rate for a standard package of 3 sessions."
    )

    # Logistics & Scheduling
    duration_minutes = models.PositiveIntegerField(
        default=30,
        help_text="Typical duration required in the clinic schedule."
    )
    recommended_interval_days = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="Optimal wait time before a follow-up or maintenance treatment."
    )

    # FIXED: Replaced ForeignKey with ManyToManyField to support multi-location machines/availability
    available_at = models.ManyToManyField(
        Clinic,
        blank=True,
        related_name="treatments_offered",
        help_text="Clinics where this treatment or specific machine is available."
    )

    # Metadata
    is_active = models.BooleanField(
        default=True,
        help_text="Uncheck this instead of deleting treatments to preserve historical data."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured_image = models.ImageField(
        upload_to="treatments/gallery/%Y/%m/",
        max_length=512,
        blank=True,
        null=True,
        help_text="Primary display photo for marketing. Requires 'Pillow' library."
    )

    class Meta:
        ordering = ['category', 'name']
        verbose_name = "Treatment"
        verbose_name_plural = "Treatments"

    def __str__(self):
        return f"{self.name} (${self.base_price})"

    def save(self, *args, **kwargs):
        # Cleaned up args tuple pattern mismatch (*from_args -> *args)
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Lead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20)

    # Contextual Connections
    preferred_clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, null=True, blank=True,
                                         related_name="leads_preferred_clinic")

    # Pro-tip: Consider changing interested_treatment to a ForeignKey(Treatment) down the line
    # if you want leads perfectly grouped by your existing services!
    interested_treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE, null=True, blank=True,
                                             related_name="leads_interested_treatment")
    estimated_value = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    # Lifecycle Tracking
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True,
                               related_name="leads_status")
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.interested_treatment}"
