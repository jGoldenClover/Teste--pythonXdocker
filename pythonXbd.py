


mostrarTabela = supabase.table('users').select('name' , 'plano' , 'email').execute()

print(mostrarTabela)