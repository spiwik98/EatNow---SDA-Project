from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='image',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='menu_images/'),
        ),
    ]
