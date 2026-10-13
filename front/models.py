import os
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


def blog_image_directory_path(instance, filename):
    """
    Generates a clean path: uploads/blogs/{blog-slug}/{uuid}.{ext}
    Fallback to 'untitled' if the parent blog slug hasn't been set yet.
    """
    blog_slug = instance.blog.slug if (instance.blog and instance.blog.slug) else "untitled"
    ext = os.path.splitext(filename)[1].lower()
    unique_filename = f"{uuid.uuid4()}{ext}"
    return os.path.join("uploads", "blogs", blog_slug, unique_filename)


class Blog(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, blank=True, help_text="URL-friendly identifier")
    writer = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="blog_posts"
    )
    date_posted = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_published = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_posted']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class BlockType(models.Model):
    """
    Defines what kind of layout block this is via database records.
    - Name: "Standard Content", Template Path: "blog/partials/content.html"
    - Name: "Google AdSense",    Template Path: "blog/partials/ad.html"
    - Name: "Newsletter Signup", Template Path: "blog/partials/newsletter.html"
    """
    name = models.CharField(max_length=50, unique=True)
    template_path = models.CharField(
        max_length=255,
        help_text="The internal directory path to the HTML partial file (e.g., 'blog/partials/content.html')."
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class BlogSection(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="sections"
    )

    # FIXED: Re-inserted the vital structural link connecting the section to its type!
    block_type = models.ForeignKey(
        BlockType,
        on_delete=models.PROTECT,
        related_name="sections"
    )

    sort_order = models.PositiveIntegerField(
        default=0,
        help_text="Controls the chronological display sequence of sections within the blog."
    )

    image = models.ImageField(
        upload_to=blog_image_directory_path,
        max_length=512,
        null=True,
        blank=True,
        help_text="Optional section header image or structural media asset."
    )
    image_url = models.URLField(
        max_length=1000,
        null=True,
        blank=True,
        help_text="Alternative option: link an external image URL instead of uploading a local file."
    )

    # Catch-all identifier token (can hold an Ad slot ID, a YouTube ID, or a Form ID for your partials)
    meta_identifier = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Contextual token used by the sub-template (e.g. ad slot hashes or video IDs)."
    )

    content = models.TextField(
        null=True,
        blank=True,
        help_text="Main content block text or markdown formatting."
    )

    class Meta:
        ordering = ['sort_order']
        verbose_name = "Blog Section"
        verbose_name_plural = "Blog Sections"

    def __str__(self):
        return f"Section {self.sort_order} ({self.block_type.name}) for: {self.blog.name}"

    @property
    def active_image_source(self):
        """Returns the direct file URL if available, otherwise falls back to the external path string."""
        return self.image.url if self.image else self.image_url
