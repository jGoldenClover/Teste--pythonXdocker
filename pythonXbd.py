

from supabase import create_client, Client


supabase: Client = create_client('https://hlcnqtihzllrialblxwb.supabase.co', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhsY25xdGloemxscmlhbGJseHdiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTIwMTMxNzEsImV4cCI6MjAyNzU4OTE3MX0.zXMjouXUUyIh7xXigfjvjYL4omPQcTE606omzRKJme8')

mostrarTabela = supabase.table('users').select('name' , 'plano' , 'email' ).execute()

print(mostrarTabela)