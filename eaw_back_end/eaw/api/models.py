from audioop import maxpp
from operator import truediv
from django.db import models


# All the API Version 1 Tables are constructed here
class CategoriesEntities(models.Model):
    id = models.PositiveBigIntegerField(max_length=20, primary_key=True)
    name = models.CharField(max_length=500, null=True)
    search_keywords = models.CharField(max_length=500, null=True)
    type = models.CharField(max_length=100, null=False, default=" ")
    thirdparty_id = models.CharField(max_length=500, null=True)
    vendor_id = models.PositiveBigIntegerField(max_length=20, null=True)
    user_id = models.PositiveBigIntegerField(max_length=20, null=True)
    related_to = models.PositiveBigIntegerField(max_length=20, null=True)
    is_active = models.IntegerField(max_length=1, null=False, default=1)
    meta = models.TextField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    related_to1 = models.PositiveBigIntegerField(max_length=20, null=True)
    related_to2 = models.PositiveBigIntegerField(max_length=20, null=True)
    related_to3 = models.PositiveBigIntegerField(max_length=20, null=True)
    related_to4 = models.PositiveBigIntegerField(max_length=20, null=True)
    is_pending = models.IntegerField(max_length=11, default=1, null=False)
    dealer_id = models.PositiveIntegerField(max_length=100, null=True)
    is_featured = models.IntegerField(max_length=11, null=True, default=0)
    featured_date = models.DateTimeField(null=True)


class CategoryEntities(models.Model):
    id = models.PositiveBigIntegerField(max_length=20, primary_key=True)
    name = models.CharField(max_length=500, null=True)
    search_keywords = models.CharField(max_length=500, null=True)
    type = models.CharField(max_length=100, null=False, default=" ")
    thirdparty_id = models.CharField(max_length=500, null=True)
    vendor_id = models.PositiveBigIntegerField(max_length=20, null=True)
    user_id = models.PositiveBigIntegerField(max_length=20, null=True)
    related_to = models.PositiveBigIntegerField(max_length=20, null=True)
    is_active = models.IntegerField(max_length=1, null=False, default=1)
    meta = models.TextField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    related_to1 = models.PositiveBigIntegerField(max_length=20, null=True)
    related_to2 = models.PositiveBigIntegerField(max_length=20, null=True)
    related_to3 = models.PositiveBigIntegerField(max_length=20, null=True)
    related_to4 = models.PositiveBigIntegerField(max_length=20, null=True)
    is_pending = models.IntegerField(max_length=11, default=1, null=False)
    dealer_id = models.IntegerField(max_length=100, null=True)
    is_featured = models.IntegerField(max_length=11, null=True, default=0)
    featured_date = models.DateTimeField(null=True)


class Entities(models.Model):
    id = models.PositiveBigIntegerField(max_length=20, primary_key=True)
    name = models.CharField(max_length=500, null=True)
    search_keywords = models.CharField(max_length=500, null=True)
    type = models.CharField(max_length=100, null=False, default=" ")
    thirdparty_id = models.CharField(max_length=500, null=True)
    vendor_id = models.PositiveBigIntegerField(max_length=20, null=True)
    user_id = models.PositiveBigIntegerField(max_length=20, null=True)
    related_to = models.PositiveBigIntegerField(max_length=20, null=True)
    is_active = models.IntegerField(max_length=1, null=False, default=1)
    meta = models.TextField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    related_to1 = models.PositiveBigIntegerField(max_length=20, null=True)
    related_to2 = models.PositiveBigIntegerField(max_length=20, null=True)
    related_to3 = models.PositiveBigIntegerField(max_length=20, null=True)
    related_to4 = models.PositiveBigIntegerField(max_length=20, null=True)
    is_pending = models.IntegerField(max_length=11, default=1, null=False)
    dealer_id = models.IntegerField(max_length=100, null=True)
    is_featured = models.IntegerField(max_length=11, null=True, default=0)
    featured_date = models.DateTimeField(null=True)
    


class EntitiesRelation(models.Model):
    id = models.BigIntegerField(max_length=20, primary_key=True)
    entity_id = models.ForeignKey(Entities, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now_add=True)
    
class InventoryEntities(models.Model):
    id = models.PositiveBigIntegerField(max_length=20, primary_key=True)
    name = models.CharField(max_length=500, null=True)
    search_keywords = models.CharField(max_length=500, null=True)
    type = models.CharField(max_length=100, null=False, default=" ")
    thirdparty_id = models.CharField(max_length=500, null=True)
    vendor_id = models.PositiveBigIntegerField(max_length=20, null=True)
    user_id = models.PositiveBigIntegerField(max_length=20, null=True)
    related_to = models.PositiveBigIntegerField(max_length=20, null=True)
    is_active = models.IntegerField(max_length=1, null=False, default=1)
    meta = models.TextField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    related_to1 = models.PositiveBigIntegerField(max_length=20, null=True)
    related_to2 = models.PositiveBigIntegerField(max_length=20, null=True)
    related_to3 = models.PositiveBigIntegerField(max_length=20, null=True)
    related_to4 = models.PositiveBigIntegerField(max_length=20, null=True)
    is_pending = models.IntegerField(max_length=11, default=1, null=False)
    dealer_id = models.IntegerField(max_length=100, null=True)
    is_featured = models.IntegerField(max_length=11, null=True, default=0)
    featured_date = models.DateTimeField(null=True)
    
class Migrations(models.Model):
    id = models.PositiveIntegerField(max_length=20, primary_key=True)
    migration = models.CharField(max_length=255, null=False, default=None)
    batch = models.IntegerField(max_length=11, null=False, default=None)
   
class ModelsEntities(models.Model):
    id = models.PositiveIntegerField(max_length=20, primary_key=True)
    name = models.CharField(max_length=500, null=True)
    search_keywords = models.CharField(max_length=500, null=True)
    type = models.CharField(max_length=100, null=False, default=" ")
    thirdparty_id = models.CharField(max_length=500, null=True)
    vendor_id = models.PositiveBigIntegerField(max_length=20, null=True)
    user_id = models.PositiveBigIntegerField(max_length=20, null=True)
    related_to = models.PositiveBigIntegerField(max_length=20, null=True)
    is_active = models.IntegerField(max_length=1, null=False, default=1)
    meta = models.TextField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    related_to1 = models.PositiveBigIntegerField(max_length=20, null=True)
    related_to2 = models.PositiveBigIntegerField(max_length=20, null=True)
    related_to3 = models.PositiveBigIntegerField(max_length=20, null=True)
    related_to4 = models.PositiveBigIntegerField(max_length=20, null=True)
    is_pending = models.IntegerField(max_length=11, default=1, null=False)
    dealer_id = models.IntegerField(max_length=100, null=True)
    is_featured = models.IntegerField(max_length=11, null=True, default=0)
    featured_date = models.DateTimeField(null=True)

class Permissions(models.Model):
    id = models.PositiveIntegerField(max_length=10, primary_key=True)
    name = models.CharField(max_length=255, null=True)
    guard_name = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(null=False, default=None)
    updated_at = models.DateTimeField(null=False, default=None)
    

class ModelHasPermissions(models.Model):
    permission_id = models.ForeignKey(Permissions, on_delete=models.CASCADE)
    model_type = models.CharField(max_length=255, null=True)
    model_id = models.PositiveIntegerField(max_length=20, null=True)
    
class Roles(models.Model):
    id = models.PositiveIntegerField(max_length=10, primary_key=True)
    name = models.CharField(max_length=255, null=True)
    guard_name = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(null=False, default=None)
    updated_at = models.DateTimeField(null=False, default=None)

class ModelHasRoles(models.Model):
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE)
    model_type = models.CharField(max_length=255, null=True)
    model_id = models.PositiveIntegerField(max_length=20, null=True)

class RoleHasPermissions(models.Model):
    permission_id = models.ForeignKey(Permissions, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE)
   
class Reports(models.Model):
    id = models.PositiveBigIntegerField(max_length=20, primary_key=True)
    dealer_id = models.PositiveBigIntegerField(max_length=20)
    month = models.DateField(null=False)
    impression = models.PositiveBigIntegerField(max_length=20, null=False, default=0)
    clicks = models.PositiveBigIntegerField(max_length=20, null=False, default=0)
    lead_count = models.PositiveBigIntegerField(max_length=20, null=False, default=0)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)
    
class ReportsTopListing(models.Model):
    pass


class ReportLeads(models.Model):
    pass


class ReportTopCountries(models.Model):
    pass


class ReportTopCustomers(models.Model):
    pass


class ReportTopQueries(models.Model):
    pass


# *** To be Studied ***
# class cache(models.Model):
#     pass

# class subscriptions(models.Model):
#     pass

# class telescope_entries(models.Model):
#     pass

# class telescope_entries_tags(models.Model):
#     pass

# class telescope_monitoring(models.Model):
#     pass

# class tracker_agents(models.Model):
#     pass

# class tracker_connections(models.Model):
#     pass

# class tracker_cookies(models.Model):
#     pass

# class tracker_devices(models.Model):
#     pass

# class tracker_domains(models.Model):
#     pass

# class tracker_errors(models.Model):
#     pass

# class tracker_events(models.Model):
#     pass

# class tracker_events_log(models.Model):
#     pass

# class tracker_geoip(models.Model):
#     pass

# class tracker_languages(models.Model):
#     pass

# class tracker_log(models.Model):
#     pass

# class tracker_paths(models.Model):
#     pass

# class tracker_queries(models.Model):
#     pass

# class tracker_referers(models.Model):
#     pass

# class tracker_referers_search_terms(models.Model):
#     pass

# class tracker_routes(models.Model):
#     pass

# class tracker_route_paths(models.Model):
#     pass

# class tracker_route_path_parameters(models.Model):
#     pass

# class tracker_sessions(models.Model):
#     pass

# class tracker_sql_queries(models.Model):
#     pass

# class tracker_sql_queries_log(models.Model):
#     pass

# class tracker_sql_query_bindings(models.Model):
#     pass

# class tracker_sql_query_bindings_parameters(models.Model):
#     pass

# class tracker_system_classes(models.Model):
#     pass

class Users(models.Model):
    id = models.PositiveBigIntegerField(max_length = 20, primary_key = True)
    name = models.CharField(max_length = 500, null = True)
    company_name = models.CharField(max_length = 100, null = False, default = None)
    email = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=100, null=False, default=None)
    email_verified_at = models.DateTimeField(null=False, default=None)
    password = models.CharField(null=False, default=None, max_length=255)
    remember_token = models.CharField(max_length=100, null=False, default=None)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    is_dealer = models.IntegerField(max_length=4, null=False, default=0)
    is_admin = models.IntegerField(max_length=4, null=False, default=0)
    stripe_id = models.CharField(max_length=255, null=False, default=None)
    card_brand = models.CharField(max_length=255, null=False, default=None)
    card_last_four = models.CharField(max_length=4, null=False, default=None)
    trial_ends_at = models.DateTimeField(null=False, default=None)
    package = models.CharField(max_length=100, null=False, default='Free')
    from_name = models.CharField(max_length=100, null=False, default=None)
    from_email = models.CharField(max_length=100, null=False, default=None)