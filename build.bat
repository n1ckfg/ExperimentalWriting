@echo off

set BUILD_TARGET=nick_corpus_combo.txt
cd /D %~dp0

del %BUILD_TARGET%

copy /b corpora-orig\nick_corpus_drama.txt+corpora-orig\harry_corpus_poems.txt+corpora-found\corpus_cinema_scifi.txt %BUILD_TARGET%

@pause
