# Add this to your .bashrc/.zshrc/.whatever
function goto() {
    if [[ $1 == "" ]]; then 
        echo "You did not supply a path alias, but that's okay - you're only human"
    else
        if [[ $(python3 ~/projects/personal/goto/g2dict.py -p $1) == "True" ]]; then
            echo "Jumping to" $1
            cd $(python3 ~/projects/personal/goto/g2dict.py $1)
        else
            echo "This path alias was not found in the dictionary"
        fi
    fi
}
