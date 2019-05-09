from django.shortcuts import render
from django.db import connection
from django.views import View

# Create your views here.


class SearchView(View):
    template_name = 'users.html'

    def get(self, request, *args, **kwargs):
        text = (request.GET.get('text') or '').strip()

        sql = """
        SELECT name 
        FROM users_user
        """
        if text:
            if "'" in text:
                pass
            else:
                sql += f"WHERE name LIKE '{text}'"
            # Василий' UNION SELECT surname FROM users_user WHERE name LIKE 'Василий


        print(sql)

        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()

        rows = [row[0] for row in rows]

        context = {
            'rows': rows,
        }

        return render(request, self.template_name, context)