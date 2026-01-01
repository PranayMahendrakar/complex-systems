"""
Autonomous Complex Systems Discovery Platform
AI for identifying and characterizing unknown complex systems
Author: Pranay M
"""

import ollama
import json
import math
import random
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Tuple
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.tree import Tree
from rich.prompt import Prompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn
import sys

console = Console()
MODEL = "llama3.2"
DATA_DIR = Path("complex_systems_data")
DATA_DIR.mkdir(exist_ok=True)


@dataclass
class ComplexSystem:
    """Representation of a discovered complex system"""
    id: str
    name: str
    domain: str  # physical, biological, social, economic, technological, hybrid
    scale: str  # micro, meso, macro, multi-scale
    components: List[str]
    interactions: List[Dict]
    emergent_properties: List[str]
    dynamics: str  # linear, nonlinear, chaotic, edge-of-chaos
    discovered: str = field(default_factory=lambda: datetime.now().isoformat())
    confidence: float = 0.5


@dataclass
class SystemSignature:
    """Signature patterns indicating a complex system"""
    pattern_name: str
    domain: str
    indicators: List[str]
    required_data: List[str]
    detection_method: str
    false_positive_rate: float


class PatternLibrary:
    """Library of complex system signatures"""
    
    SIGNATURES = [
        SystemSignature(
            pattern_name="Power Law Distribution",
            domain="universal",
            indicators=["Heavy-tailed distribution", "Scale-free structure", "Preferential attachment"],
            required_data=["Size/frequency data", "Network degree distribution"],
            detection_method="Log-log plot linearity test",
            false_positive_rate=0.15
        ),
        SystemSignature(
            pattern_name="Self-Organized Criticality",
            domain="universal",
            indicators=["Avalanche dynamics", "1/f noise", "Power law events"],
            required_data=["Event size time series", "Spatial patterns"],
            detection_method="Avalanche size distribution analysis",
            false_positive_rate=0.2
        ),
        SystemSignature(
            pattern_name="Emergent Collective Behavior",
            domain="biological/social",
            indicators=["Phase transitions", "Synchronization", "Swarm intelligence"],
            required_data=["Agent-level data", "Collective outputs"],
            detection_method="Order parameter analysis",
            false_positive_rate=0.1
        ),
        SystemSignature(
            pattern_name="Feedback Loops",
            domain="universal",
            indicators=["Amplification/dampening", "Delayed responses", "Oscillations"],
            required_data=["Input-output time series", "Causal relationships"],
            detection_method="Transfer function analysis",
            false_positive_rate=0.12
        ),
        SystemSignature(
            pattern_name="Network Motifs",
            domain="biological/social",
            indicators=["Recurring subgraphs", "Functional modules", "Hierarchical structure"],
            required_data=["Network topology", "Interaction types"],
            detection_method="Subgraph enumeration and comparison",
            false_positive_rate=0.08
        )
    ]
    
    def get_signatures(self, domain: str = "all") -> List[SystemSignature]:
        if domain == "all":
            return self.SIGNATURES
        return [s for s in self.SIGNATURES if s.domain == domain or s.domain == "universal"]


class SystemDetector:
    """Detect complex systems in data or descriptions"""
    
    def analyze_for_complexity(self, description: str, data_summary: str = "") -> str:
        """Analyze if description indicates a complex system"""
        prompt = f"""Analyze this for signs of a complex system:

DESCRIPTION:
{description}

DATA SUMMARY:
{data_summary if data_summary else "Not provided"}

Look for indicators of complexity:
1. **Multiple Interacting Components**: Many parts that affect each other
2. **Nonlinear Dynamics**: Disproportionate cause-effect relationships
3. **Emergence**: System-level properties not in components
4. **Self-Organization**: Spontaneous pattern formation
5. **Adaptation**: Learning and evolution
6. **Feedback Loops**: Circular causation
7. **Scale Invariance**: Similar patterns at different scales
8. **Phase Transitions**: Sudden qualitative changes

For each indicator found:
- Evidence present
- Confidence level
- Alternative explanation

Conclude: Is this a complex system? Confidence?
Format key findings as JSON."""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']
    
    def characterize_system(self, system_description: str) -> str:
        """Characterize a discovered complex system"""
        prompt = f"""Characterize this complex system:

SYSTEM: {system_description}

Determine:
1. **Domain Classification**: Physical/biological/social/economic/technological/hybrid
2. **Scale**: Micro/meso/macro/multi-scale
3. **Component Types**: What are the interacting parts?
4. **Interaction Types**: How do components interact?
5. **Emergent Properties**: What arises from interactions?
6. **Dynamics Type**: Linear/nonlinear/chaotic/edge-of-chaos
7. **Boundaries**: What defines system boundaries?
8. **Environment**: How does it interact with surroundings?
9. **Stability**: Is it stable, metastable, or unstable?
10. **Evolution**: How does it change over time?

Provide comprehensive characterization."""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']


class SystemHunter:
    """Actively search for unknown complex systems"""
    
    def hunt_in_domain(self, domain: str) -> str:
        """Search for undiscovered complex systems in a domain"""
        prompt = f"""Actively search for potentially unknown complex systems in:

DOMAIN: {domain}

Explore:
1. **Known Systems**: What complex systems are well-studied here?
2. **Candidate Systems**: What phenomena might be complex systems but aren't recognized as such?
3. **Interface Systems**: Complex systems at boundaries between domains
4. **Emergent Digital Systems**: New systems arising from technology
5. **Hidden Systems**: Systems that might exist but are hard to observe

For each candidate:
- Why it might be a complex system
- What data would reveal it
- How to study it
- Potential implications if confirmed

Be creative and think beyond conventional categorizations."""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']
    
    def cross_domain_search(self, domains: List[str]) -> str:
        """Search for complex systems spanning multiple domains"""
        prompt = f"""Search for complex systems spanning these domains:

DOMAINS: {json.dumps(domains)}

Look for:
1. **Cross-Domain Systems**: Systems with components in multiple domains
2. **Emergent Interfaces**: Novel systems at domain boundaries
3. **Isomorphic Patterns**: Same complex system pattern in different domains
4. **Coupled Systems**: How systems in different domains interact
5. **Meta-Systems**: Higher-level systems composed of domain-specific systems

For each discovery:
- What the system is
- How it spans domains
- Why it wasn't recognized before
- Research approach needed"""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']


class SystemModeler:
    """Model and predict complex system behavior"""
    
    def propose_model(self, system: str, observations: str) -> str:
        """Propose a model for a complex system"""
        prompt = f"""Propose a model for this complex system:

SYSTEM: {system}
OBSERVATIONS: {observations}

Design:
1. **Model Type**: Agent-based, network, differential equations, cellular automata, hybrid
2. **State Variables**: What to track
3. **Dynamics**: Rules governing evolution
4. **Parameters**: Key parameters and their meaning
5. **Initialization**: How to set initial conditions
6. **Validation**: How to test against real data
7. **Predictions**: What the model would predict
8. **Limitations**: Known simplifications and gaps

Provide a detailed model specification."""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']
    
    def predict_behavior(self, system: str, scenario: str) -> str:
        """Predict system behavior under a scenario"""
        prompt = f"""Predict complex system behavior:

SYSTEM: {system}
SCENARIO: {scenario}

Predict:
1. **Short-term Response**: Immediate effects
2. **Transient Dynamics**: Path to new state
3. **Long-term State**: Eventual outcome
4. **Critical Points**: Potential phase transitions
5. **Feedback Effects**: How responses feed back
6. **Uncertainty**: Confidence and key unknowns
7. **Tipping Points**: Where might small changes cause large effects?

Use complex systems reasoning and be explicit about assumptions."""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']


class UniversalPatternFinder:
    """Find universal patterns across complex systems"""
    
    def find_universalities(self, systems: List[str]) -> str:
        """Find universal patterns across systems"""
        prompt = f"""Find universal patterns across these complex systems:

SYSTEMS: {json.dumps(systems)}

Search for:
1. **Structural Universals**: Similar network structures, hierarchies
2. **Dynamic Universals**: Similar time evolution patterns
3. **Statistical Universals**: Power laws, distributions
4. **Organizational Universals**: Modularity, nestedness
5. **Critical Universals**: Phase transition behaviors
6. **Information Universals**: Information processing patterns

For each universal found:
- What the pattern is
- Which systems exhibit it
- Why it might be universal
- Exceptions and boundary conditions"""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']


class ComplexSystemsDatabase:
    """Store discovered complex systems"""
    
    def __init__(self):
        self.db_file = DATA_DIR / "systems.json"
        self.systems = self._load()
    
    def _load(self) -> Dict:
        if self.db_file.exists():
            return json.loads(self.db_file.read_text())
        return {}
    
    def _save(self):
        self.db_file.write_text(json.dumps(self.systems, indent=2, default=str))
    
    def add_system(self, system: ComplexSystem):
        self.systems[system.id] = asdict(system)
        self._save()
    
    def get_systems(self, domain: str = None) -> List[dict]:
        if domain:
            return [s for s in self.systems.values() if s.get('domain') == domain]
        return list(self.systems.values())


# ============= CLI Interface =============

def show_banner():
    banner = """
╔══════════════════════════════════════════════════════════════╗
║    🔮 Autonomous Complex Systems Discovery Platform 🔮       ║
║         Discovering Hidden Complexity in the World           ║
║                    Author: Pranay M                          ║
╚══════════════════════════════════════════════════════════════╝
    """
    console.print(Panel(banner, style="bold magenta"))


def show_menu():
    table = Table(title="Complex Systems Discovery", show_header=False, box=None)
    table.add_column("Option", style="cyan")
    table.add_column("Description")
    
    table.add_row("1", "🔍 Analyze for Complexity")
    table.add_row("2", "📊 Characterize System")
    table.add_row("3", "🎯 Hunt in Domain")
    table.add_row("4", "🌐 Cross-Domain Search")
    table.add_row("5", "🧮 Propose Model")
    table.add_row("6", "🔮 Predict Behavior")
    table.add_row("7", "🌌 Find Universals")
    table.add_row("8", "📚 View Signature Library")
    table.add_row("9", "💾 View Discovered Systems")
    table.add_row("0", "🚪 Exit")
    
    console.print(table)


db = ComplexSystemsDatabase()


def analyze_complexity():
    console.print("\n[cyan]Describe the phenomenon to analyze:[/cyan]")
    lines = []
    console.print("[dim]Enter description (empty line to finish):[/dim]")
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    
    description = "\n".join(lines)
    data_summary = Prompt.ask("Data summary (optional)", default="")
    
    detector = SystemDetector()
    
    with Progress(SpinnerColumn(), TextColumn("Analyzing...")) as progress:
        task = progress.add_task("", total=None)
        analysis = detector.analyze_for_complexity(description, data_summary)
    
    console.print(Panel(analysis, title="Complexity Analysis"))


def characterize_system():
    system_desc = Prompt.ask("Describe the system")
    
    detector = SystemDetector()
    
    with Progress(SpinnerColumn(), TextColumn("Characterizing...")) as progress:
        task = progress.add_task("", total=None)
        characterization = detector.characterize_system(system_desc)
    
    console.print(Panel(characterization, title="System Characterization"))


def hunt_domain():
    domain = Prompt.ask("Domain to search", default="urban systems")
    
    hunter = SystemHunter()
    
    with Progress(SpinnerColumn(), TextColumn("Hunting...")) as progress:
        task = progress.add_task("", total=None)
        discoveries = hunter.hunt_in_domain(domain)
    
    console.print(Panel(discoveries, title=f"Complex Systems in {domain}"))


def cross_domain():
    domains_input = Prompt.ask("Domains (comma-separated)", 
                               default="biology,technology,economics")
    domains = [d.strip() for d in domains_input.split(",")]
    
    hunter = SystemHunter()
    
    with Progress(SpinnerColumn(), TextColumn("Searching...")) as progress:
        task = progress.add_task("", total=None)
        discoveries = hunter.cross_domain_search(domains)
    
    console.print(Panel(discoveries, title="Cross-Domain Complex Systems"))


def propose_model():
    system = Prompt.ask("System to model")
    observations = Prompt.ask("Key observations")
    
    modeler = SystemModeler()
    
    with Progress(SpinnerColumn(), TextColumn("Designing model...")) as progress:
        task = progress.add_task("", total=None)
        model = modeler.propose_model(system, observations)
    
    console.print(Panel(model, title="Proposed Model"))


def predict_behavior():
    system = Prompt.ask("System")
    scenario = Prompt.ask("Scenario to predict")
    
    modeler = SystemModeler()
    
    with Progress(SpinnerColumn(), TextColumn("Predicting...")) as progress:
        task = progress.add_task("", total=None)
        prediction = modeler.predict_behavior(system, scenario)
    
    console.print(Panel(prediction, title="Behavior Prediction"))


def find_universals():
    systems_input = Prompt.ask("Systems to compare (comma-separated)",
                               default="cities,ant colonies,neurons,markets")
    systems = [s.strip() for s in systems_input.split(",")]
    
    finder = UniversalPatternFinder()
    
    with Progress(SpinnerColumn(), TextColumn("Finding universals...")) as progress:
        task = progress.add_task("", total=None)
        universals = finder.find_universalities(systems)
    
    console.print(Panel(universals, title="Universal Patterns"))


def view_signatures():
    library = PatternLibrary()
    
    table = Table(title="Complex System Signatures")
    table.add_column("Pattern", style="cyan")
    table.add_column("Domain")
    table.add_column("Indicators")
    
    for sig in library.get_signatures():
        table.add_row(
            sig.pattern_name,
            sig.domain,
            ", ".join(sig.indicators[:2])
        )
    
    console.print(table)


def view_discovered():
    systems = db.get_systems()
    
    if not systems:
        console.print("[yellow]No systems discovered yet[/yellow]")
        return
    
    table = Table(title="Discovered Complex Systems")
    table.add_column("ID", style="cyan")
    table.add_column("Name")
    table.add_column("Domain")
    table.add_column("Confidence")
    
    for sys in systems:
        table.add_row(
            sys.get('id', '')[:10],
            sys.get('name', ''),
            sys.get('domain', ''),
            f"{sys.get('confidence', 0):.0%}"
        )
    
    console.print(table)


def main():
    show_banner()
    
    try:
        ollama.list()
    except Exception:
        console.print("[red]Error: Ollama not running. Start with: ollama serve[/red]")
        sys.exit(1)
    
    while True:
        show_menu()
        choice = Prompt.ask("\nSelect option", default="0")
        
        actions = {
            "1": analyze_complexity, "2": characterize_system, "3": hunt_domain,
            "4": cross_domain, "5": propose_model, "6": predict_behavior,
            "7": find_universals, "8": view_signatures, "9": view_discovered
        }
        
        if choice == "0":
            console.print("[yellow]Complexity is everywhere! 🔮[/yellow]")
            break
        elif choice in actions:
            actions[choice]()
        else:
            console.print("[red]Invalid option[/red]")
        
        console.print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()
