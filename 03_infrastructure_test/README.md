To deploy
- Add AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY to vagrant file
- Then run 'vagrant up'
- Then run 'vagrant ssh'

To destroy
- export AWS_ACCESS_KEY_ID= 
- export AWS_SECRET_ACCESS_KEY=
 Run terraform destroy -auto-approve -lock=false
