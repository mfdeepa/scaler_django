from abc import ABC
from django.utils import timezone
from django.db import models


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_num = models.IntegerField()
    password = models.CharField(max_length=12)

class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=100)
    users = models.ManyToManyField(User, through='UserGroup', related_name='user_groups')
    group_admin_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_group')

class UserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(timezone.now())

    class Meta:
        unique_together = ('user', 'group')
class ExpenseType(models.IntegerChoices):
    SETTLE_UP = 0
    EXPENSE = 1

class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    expense_name = models.CharField(max_length=100)
    expense_type = models.IntegerField(choices=ExpenseType.choices, default=ExpenseType.SETTLE_UP)
    #expense_type = models.ForeignKey(ExpenseType,on_delete=models.CASCADE)
    expense_amount = models.IntegerField()
    description = models.TextField()
    create_date = models.DateTimeField()
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)



class UserExpenseType(models.IntegerChoices):
    PAID = 0
    OWE = 1

class UserExpense(ABC):
    expense_id = models.ForeignKey(Expense, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    user_expense_type = models.IntegerField(choices=UserExpenseType.choices)
    #user_expense_type = models.ForeignKey(UserExpenseType, on_delete=models.CASCADE)

