from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory
from groq_ai.client import get_car_ai_bio

def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )

@receiver(pre_save, sender=Car)
def pre_save(sender, instance, **kwargs):
    # Só gera bio se não existir e se for um novo carro (não update)
    if not instance.bio and not instance.pk:
        ai_bio = get_car_ai_bio(
            str(instance.model),
            str(instance.brand),
            instance.model_year or ""
        )
        instance.bio = ai_bio

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()