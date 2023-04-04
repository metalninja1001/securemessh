import paramiko
import typer

app = typer.Typer()

@app.command()
def send_message(server: str = typer.Option(..., prompt=True),
                 username: str = typer.Option(..., prompt=True),
                 password: str = typer.Option(..., prompt=True, hide_input=True)):
    # Set up SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to server
    ssh.connect(server, username=username, password=password)

    # Prompt for message to send
    message = typer.edit()

    # Send message
    stdin, stdout, stderr = ssh.exec_command(f'echo "{message}" | nc localhost 443')

    # Print response
    response = stdout.read().decode()
    print(response)

    # Close connection
    ssh.close()

if __name__ == "__main__":
    app()