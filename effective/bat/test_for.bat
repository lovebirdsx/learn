set LIST="hello"
set LIST=%LIST%;"wolrd"

for %%a in (%LIST%) do (
    echo %%a
)