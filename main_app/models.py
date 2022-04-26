from django.db import models

class brand (models.Model):
    brand_id=models.IntegerField(unique=True, db_index=True,primary_key=True)
    brand_name=models.CharField(max_length=100)
    brand_desc=models.CharField(max_length=100)
    brand_image=models.ImageField(upload_to="pics")

class category (models.Model):
    cat_id=models.IntegerField(unique=True, db_index=True,primary_key=True)
    cat_name=models.CharField(max_length=100)
    cat_desc=models.CharField(max_length=100)
    cat_image=models.ImageField(upload_to='pics')

class product(models.Model):
    product_id = models.IntegerField(unique=True, db_index=True, primary_key=True)
    product_name = models.CharField(max_length=100)
    product_brand = models.ForeignKey(brand, on_delete=models.CASCADE)
    product_cat = models.ForeignKey(category, on_delete=models.CASCADE)

class trends (models.Model):
    trend_id=models.IntegerField(unique=True, db_index=True,primary_key=True)
    prod_trend=models.ForeignKey(product, on_delete=models.CASCADE)
    prod_cat=models.ForeignKey(category, on_delete=models.CASCADE)

class product_image(models.Model):
    image_id=models.IntegerField(unique=True, db_index=True, primary_key=True)
    prod_image=models.ForeignKey(product,on_delete=models.CASCADE)
    img1=models.ImageField(upload_to="pics")
    img2=models.ImageField(upload_to="pics")
    img3= models.ImageField(upload_to="pics")
    img4= models.ImageField(upload_to="pics")

class color(models.Model):
    color_id=models.IntegerField(unique=True, db_index=True,primary_key=True)
    prod_color_id=models.ForeignKey(product,on_delete=models.CASCADE)
    color_name=models.CharField(max_length=100)

class product_desc(models.Model):
    prod_desc_id=models.IntegerField(unique=True, db_index=True, primary_key=True)
    main_product=models.ForeignKey(product,on_delete=models.CASCADE)
    prod_color_id=models.ForeignKey(color,on_delete=models.CASCADE)
    prod_price=models.FloatField()
    prod_quanitity=models.IntegerField()
    prod_date=models.DateField()
    prodduct_image=models.ForeignKey(product_image,on_delete=models.CASCADE)

class latest (models.Model):
    latest_id=models.IntegerField(unique=True,primary_key=True,db_index=True)
    product_latest=models.ForeignKey(product,on_delete=models.CASCADE)
    prod_cat=models.ForeignKey(category, on_delete=models.CASCADE)
    prod_time=models.TimeField()

class customer(models.Model):
    cust_id=models.IntegerField(unique=True, db_index=True,primary_key=True)
    cust_name=models.CharField(max_length=100)
    cust_email=models.CharField(max_length=100)
    cust_pass=models.CharField(max_length=100)
    cust_contact=models.CharField(max_length=100)
    cust_address=models.CharField(max_length=100)

class wishlist (models.Model):
    wishlist_id=models.IntegerField(unique=True, db_index=True,primary_key=True)
    wishlist_cust=models.ForeignKey(customer, on_delete=models.CASCADE)

class wishlist_item(models.Model):
    wishlist_item_id=models.IntegerField(unique=True,primary_key=True,db_index=True)
    wishlist_id_fk=models.ForeignKey(wishlist,on_delete=models.CASCADE)
    product_wishlist_id=models.ForeignKey(product,on_delete=models.CASCADE)
    createdon=models.DateField()
    modifiedon=models.DateField()

class cart (models.Model):
    cart_id=models.IntegerField(unique=True, db_index=True,primary_key=True)
    cart_cust=models.ForeignKey(customer, on_delete=models.CASCADE)

class cart_item(models.Model):
    cart_item_id=models.IntegerField(unique=True,primary_key=True,db_index=True)
    cart_id_fk=models.ForeignKey(cart,on_delete=models.CASCADE)
    product_cart_id=models.ForeignKey(product,on_delete=models.CASCADE)
    created_on=models.DateField()
    modified_on=models.DateField()

class order(models.Model):
    order_id=models.IntegerField(unique=True,primary_key=True,db_index=True)
    order_prod_id=models.ForeignKey(product,on_delete=models.CASCADE)
    order_quantity=models.IntegerField()
    order_price=models.FloatField()

class sales(models.Model):
    sales_id=models.IntegerField(unique=True,primary_key=True,db_index=True)
    sales_order_id=models.ForeignKey(order,on_delete=models.CASCADE)
    sales_payment_mode=models.CharField(max_length=100)

class cat1(models.Model):
    cat_id=models.IntegerField(unique=True,primary_key=True,db_index=True)
    car_name=models.CharField(max_length=100)
    img1=models.ImageField(upload_to='pics')
    img2=models.ImageField(upload_to='pics')
    img3=models.ImageField(upload_to='pics')


class cat2(models.Model):
    cat2_id=models.IntegerField(unique=True,primary_key=True,db_index=True)
    car2_name=models.CharField(max_length=100)
    img1=models.ImageField(upload_to='pics')
    img2=models.ImageField(upload_to='pics')
    img3=models.ImageField(upload_to='pics')

class cat3(models.Model):
    cat3_id=models.IntegerField(unique=True,primary_key=True,db_index=True)
    car3_name=models.CharField(max_length=100)
    img1=models.ImageField(upload_to='pics')
    img2=models.ImageField(upload_to='pics')
    img3=models.ImageField(upload_to='pics')

class cat4(models.Model):
    cat4_id=models.IntegerField(unique=True,primary_key=True,db_index=True)
    car4_name=models.CharField(max_length=100)
    img1=models.ImageField(upload_to='pics')
    img2=models.ImageField(upload_to='pics')
    img3=models.ImageField(upload_to='pics')

class cat5(models.Model):
    cat5_id=models.IntegerField(unique=True,primary_key=True,db_index=True)
    car5_name=models.CharField(max_length=100)
    img1=models.ImageField(upload_to='pics')
    img2=models.ImageField(upload_to='pics')
    img3=models.ImageField(upload_to='pics')

class cat6(models.Model):
    cat6_id=models.IntegerField(unique=True,primary_key=True,db_index=True)
    car6_name=models.CharField(max_length=100)
    img1=models.ImageField(upload_to='pics')
    img2=models.ImageField(upload_to='pics')
    img3=models.ImageField(upload_to='pics')


class order_details(models.Model):
    order_id=models.IntegerField(unique=True,primary_key=True,db_index=True)
    order_prod_id=models.ForeignKey(order,on_delete=models.CASCADE)
    order_quantity=models.IntegerField()
    order_price=models.FloatField()


