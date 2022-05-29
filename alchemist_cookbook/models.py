# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Characterattribute(models.Model):
    attributeid = models.CharField(db_column='AttributeID', primary_key=True, max_length=18)  # Field name made lowercase.
    attributename = models.CharField(db_column='AttributeName', unique=True, max_length=30)  # Field name made lowercase.
    attributetype = models.CharField(db_column='AttributeType', max_length=18)  # Field name made lowercase.
    attributemeasure = models.CharField(db_column='AttributeMeasure', max_length=18, blank=True, null=True)  # Field name made lowercase.
    attributeminvalue = models.SmallIntegerField(db_column='AttributeMinValue', blank=True, null=True)  # Field name made lowercase.
    attributemaxvalue = models.PositiveSmallIntegerField(db_column='AttributeMaxValue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CharacterAttribute'


class Effect(models.Model):
    effectid = models.BigAutoField(db_column='EffectID', primary_key=True)  # Field name made lowercase.
    effectname = models.CharField(db_column='EffectName', unique=True, max_length=30)  # Field name made lowercase.
    effecttype = models.CharField(db_column='EffectType', max_length=18, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Effect'


class Effecttarget(models.Model):
    effectid = models.PositiveBigIntegerField(db_column='EffectID', primary_key=True)  # Field name made lowercase.
    attributeid = models.CharField(db_column='AttributeID', max_length=18)  # Field name made lowercase.
    effectmeasure = models.CharField(db_column='EffectMeasure', max_length=18, blank=True, null=True)  # Field name made lowercase.
    effectminvalue = models.SmallIntegerField(db_column='EffectMinValue', blank=True, null=True)  # Field name made lowercase.
    effectmaxvalue = models.PositiveSmallIntegerField(db_column='EffectMaxValue', blank=True, null=True)  # Field name made lowercase.
    effectminduration = models.PositiveSmallIntegerField(db_column='EffectMinDuration', blank=True, null=True)  # Field name made lowercase.
    effectmaxduration = models.PositiveSmallIntegerField(db_column='EffectMaxDuration', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EffectTarget'
        unique_together = (('effectid', 'attributeid'),)


class Ingredient(models.Model):
    ingredientid = models.BigAutoField(db_column='IngredientID', primary_key=True)  # Field name made lowercase.
    ingredientname = models.CharField(db_column='IngredientName', unique=True, max_length=60)  # Field name made lowercase.
    ingredientweight = models.FloatField(db_column='IngredientWeight', blank=True, null=True)  # Field name made lowercase.
    ingredientvalue = models.PositiveSmallIntegerField(db_column='IngredientValue')  # Field name made lowercase.
    ingredienteffect1 = models.PositiveBigIntegerField(db_column='IngredientEffect1', blank=True, null=True)  # Field name made lowercase.
    ingredienteffect2 = models.PositiveBigIntegerField(db_column='IngredientEffect2', blank=True, null=True)  # Field name made lowercase.
    ingredienteffect3 = models.PositiveBigIntegerField(db_column='IngredientEffect3', blank=True, null=True)  # Field name made lowercase.
    ingredienteffect4 = models.PositiveBigIntegerField(db_column='IngredientEffect4', blank=True, null=True)  # Field name made lowercase.
    ingredientlocations = models.TextField(db_column='IngredientLocations', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ingredient'


class Potion(models.Model):
    potionid = models.BigAutoField(db_column='PotionID', unique=True)  # Field name made lowercase.
    recepyid = models.CharField(db_column='RecepyID', max_length=30)  # Field name made lowercase.
    potionname = models.CharField(db_column='PotionName', max_length=60)  # Field name made lowercase.
    alchemylevel = models.PositiveIntegerField(db_column='AlchemyLevel', blank=True, null=True)  # Field name made lowercase.
    effectvaluemultiplier = models.FloatField(db_column='EffectValueMultiplier')  # Field name made lowercase.
    efeffectdurationmultiplier = models.FloatField(db_column='EfEffectDurationMultiplier', blank=True, null=True)  # Field name made lowercase.
    potionweight = models.FloatField(db_column='PotionWeight', blank=True, null=True)  # Field name made lowercase.
    potionvalue = models.PositiveSmallIntegerField(db_column='PotionValue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Potion'


class Recepy(models.Model):
    recepyid = models.CharField(db_column='RecepyID', primary_key=True, max_length=30)  # Field name made lowercase.
    recepyname = models.CharField(db_column='RecepyName', max_length=30)  # Field name made lowercase.
    recepyingredientcount = models.PositiveIntegerField(db_column='RecepyIngredientCount')  # Field name made lowercase.
    recepylevel = models.SmallIntegerField(db_column='RecepyLevel', blank=True, null=True)  # Field name made lowercase.
    recepysuccess = models.IntegerField(db_column='RecepySuccess', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Recepy'


class Recepyeffect(models.Model):
    recepyid = models.CharField(db_column='RecepyID', primary_key=True, max_length=30)  # Field name made lowercase.
    effectid = models.PositiveBigIntegerField(db_column='EffectID')  # Field name made lowercase.
    effectbasevalue = models.SmallIntegerField(db_column='EffectBaseValue', blank=True, null=True)  # Field name made lowercase.
    effectbaseduration = models.SmallIntegerField(db_column='EffectBaseDuration', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RecepyEffect'
        unique_together = (('recepyid', 'effectid'),)


class Recepyingredient(models.Model):
    recepyid = models.CharField(db_column='RecepyID', primary_key=True, max_length=30)  # Field name made lowercase.
    ingredientid = models.PositiveBigIntegerField(db_column='IngredientID')  # Field name made lowercase.
    ingredientnumber = models.PositiveIntegerField(db_column='IngredientNumber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RecepyIngredient'
        unique_together = (('recepyid', 'ingredientid'),)
