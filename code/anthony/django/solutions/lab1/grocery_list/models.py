from django.db import models

# GroceryItem model:
# - name
# - quantity
# - created_at
# - purchased


class GroceryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        if not self.purchased:
            return f"Need to buy {self.quantity} {self.name}"

        return self.name
