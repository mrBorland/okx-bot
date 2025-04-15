#!/bin/bash

# Налаштування Git
git config --global user.name "MrBorland"
git config --global user.email "borlandx54@example.com"

# Ініціалізація репозиторію (лише якщо ще не створений .git)
git init
git add .
git commit -m "Автоматичне оновлення з VPS"

# Токен GitHub
TOKEN="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"
REPO="github.com/mrBorland/okx-бот.git"

# Додавання віддаленого репозиторію
git remote remove origin 2>/dev/null
git remote add origin https://$TOKEN@$REPO

# Пуш на GitHub
git branch -M main
git push -u origin main

echo "✅ Код успішно завантажено на GitHub!"
