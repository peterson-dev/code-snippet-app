# Generated by Django 2.2.1 on 2019-05-22 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190405_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='language',
            field=models.CharField(choices=[('bash', 'Bash'), ('basic', 'Basic'), ('c', 'C'), ('css', 'CSS'), ('csharp', 'C#'), ('cpp', 'C++'), ('coffee', 'CoffeeScript'), ('clojure', 'Clojure'), ('docker', 'Docker'), ('elixir', 'Elixir'), ('fsharp', 'F#'), ('git', 'Git'), ('go', 'Go'), ('graphql', 'GraphQL'), ('html', 'HTML'), ('java', 'Java'), ('js', 'Javascript'), ('json', 'JSON'), ('monkey', 'Monkey'), ('objectivec', 'Objective-C'), ('pascal', 'Pascal'), ('perl', 'Perl'), ('php', 'PHP'), ('py', 'Python'), ('jsx', 'React JSX'), ('ruby', 'Ruby'), ('rust', 'Rust'), ('sql', 'SQL'), ('swift', 'Swift'), ('ts', 'typescript'), ('yml', 'YAML')], max_length=420),
        ),
    ]
