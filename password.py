import re
from rich.console import Console
from rich.table import Table
from rich.progress import track
import time

def assess_password_strength(password):
    console = Console()
    strength = 0
    feedback = []
    
    # Length check
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("[red]Password should be at least 8 characters long.[/red]")
    
    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("[yellow]Include at least one uppercase letter (A-Z).[/yellow]")
    
    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("[yellow]Include at least one lowercase letter (a-z).[/yellow]")
    
    # Digit check
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("[yellow]Include at least one number (0-9).[/yellow]")
    
    # Special character check
    if re.search(r"[@$!%*?&]", password):
        strength += 1
    else:
        feedback.append("[yellow]Use at least one special character (@$!%*?&).[/yellow]")
    
    # Strength rating
    if strength <= 2:
        rating = "[red]Weak[/red]"
    elif strength <= 4:
        rating = "[yellow]Moderate[/yellow]"
    else:
        rating = "[green]Strong[/green]"
    
    return {"strength": rating, "suggestions": feedback}

# Get user input and assess password
console = Console()
password = console.input("[bold cyan]Enter your password: [/bold cyan]")

console.print("\n[bold magenta]Analyzing password...[/bold magenta]")
for _ in track(range(10), description="Processing..."):
    time.sleep(0.1)

result = assess_password_strength(password)

console.print(f"\n[bold]Password Strength:[/bold] {result['strength']}")
if result["suggestions"]:
    console.print("\n[bold cyan]Suggestions to improve your password:[/bold cyan]")
    table = Table(title="Password Improvement Tips")
    table.add_column("Tip", style="cyan")
    for suggestion in result["suggestions"]:
        table.add_row(suggestion)
    console.print(table)
