class StudentRegionRouter:
    def db_for_read(self, model, **hints):
        if model._meta.db_table == 'student_north':
            return 'north_db'
        elif model._meta.db_table == 'student_south':
            return 'south_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.db_table == 'student_north':
            return 'north_db'
        elif model._meta.db_table == 'student_south':
            return 'south_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'studentregionnorth':
            return db == 'north'
        elif model_name == 'studentregionsouth':
            return db == 'south'
        return db == 'default'
