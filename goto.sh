# Add this to your .bashrc/.zshrc/.whatever
function goto() {
    if [[ $1 == "" ]]; then 
        echo "You did not supply a path alias, but that's okay - you're only human"
    else
        # Check if the dictionary entry exists
        if [[ $(python3 g2dict -p $1) == "True" ]]; then 
            echo "Jumping to" $1
            cd $(python3 g2dict $1)
        else
            echo "This path alias was not found in the dictionary"
        fi
    fi
}
