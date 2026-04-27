with open('community.html', 'r', encoding='utf-8') as f:
    html = f.read()
print('<!-- count:', html.count('<!--'))
print('--> count:', html.count('-->'))
print('<script starts:', html.count('<script'))
print('</script ends:', html.count('</script>'))
