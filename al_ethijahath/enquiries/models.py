from django.db import models


class EquipmentCategory(models.Model):
    name = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Equipment Category"
        verbose_name_plural = "Equipment Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name 


class DispatchRequest(models.Model):

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        REVIEWING = "reviewing", "Reviewing"
        CONTACTED = "contacted", "Contacted"
        IN_PROGRESS = "in_progress", "In Progress"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"

    company_name = models.CharField(max_length=200)

    contact_person = models.CharField(max_length=150)

    phone = models.CharField(max_length=30)

    equipment_category = models.ForeignKey(
        EquipmentCategory,
        on_delete=models.PROTECT,
        related_name="dispatch_requests"
    )
    photo = models.ImageField(upload_to="equipment_images/",blank=True,null=True)

    issue_description = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Dispatch Request"
        verbose_name_plural = "Dispatch Requests"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.company_name} - {self.equipment_category.name}"


class EquipmentPortfolio(models.Model):
    portfolio_image = models.ImageField(upload_to = 'portfolio_mages/')
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 255)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Equipment Portfolio"
        verbose_name_plural = "Equipment Portfolioes"

    def __str__(self):
        return f"{self.title}"

class Blog(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title