from doctest import OutputChecker


print('Hello World!')

print('Второй проект.'):

 # ввели команду для отображения состояния репозитория
git status
# и вот что Git сообщает в ответ
On branch master
No commits yet
Modified files:
  (use "git add <file>..." to include in what will be committed)
  program.py

nothing added to commit but untracked files present (use "git add" to track) 



# добавили файл "program.py"
git add program.py

# добавили все файлы
git add --all

# добавили все файлы
git add .



git status

On branch master
No commits yet
Changes to be committed: # файлы ожидают коммита
  (use "git rm --cached <file>..." to unstage)
    new file:   program.py




git commit -m "My first commit"
# сделали первый коммит
# текст комментария: "My first commit"
# комментарии лучше писать латиницей

# делаем первый коммит, в кавычках пишем комментарий
git commit -m "First commit: change program.py"

# добавили файлы в индекс Git
git add --all

# добавили эти файлы к предыдущему коммиту
git commit --amend -m "First commit: new files added"



git push