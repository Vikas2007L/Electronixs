
import tkinter as tk
from tkinter import ttk, messagebox

# ============================================================
# OPEN ELECTRONICS LAB
# Single-file Python desktop application
# ============================================================

BG = "#090e18"
SIDEBAR = "#0c1422"
PANEL = "#111b2b"
PANEL2 = "#172438"
BORDER = "#293b52"
TEXT = "#e6f0ff"
MUTED = "#8da2bc"
CYAN = "#42d9ff"
GREEN = "#35e69a"
RED = "#ff637d"
YELLOW = "#ffd166"
PURPLE = "#a997ff"


IC_DATABASE = [
    ("7400", "Quad NAND Gate", "Digital Logic", "NAND", 14),
    ("7402", "Quad NOR Gate", "Digital Logic", "NOR", 14),
    ("7404", "Hex Inverter", "Digital Logic", "NOT", 14),
    ("7408", "Quad AND Gate", "Digital Logic", "AND", 14),
    ("7432", "Quad OR Gate", "Digital Logic", "OR", 14),
    ("7486", "Quad XOR Gate", "Digital Logic", "XOR", 14),
    ("7410", "Triple 3-input NAND", "Digital Logic", "NAND", 14),
    ("7420", "Dual 4-input NAND", "Digital Logic", "NAND", 14),
    ("7427", "Triple 3-input NOR", "Digital Logic", "NOR", 14),
    ("7430", "8-input NAND", "Digital Logic", "NAND", 14),
    ("7474", "Dual D Flip-Flop", "Sequential Logic", "SEQUENTIAL", 14),
    ("7476", "Dual JK Flip-Flop", "Sequential Logic", "SEQUENTIAL", 16),
    ("74138", "3-to-8 Decoder", "Combinational", "DECODER", 16),
    ("74151", "8-to-1 Multiplexer", "Combinational", "MUX", 16),
    ("74153", "Dual 4-to-1 Multiplexer", "Combinational", "MUX", 16),
    ("74157", "Quad 2-to-1 Multiplexer", "Combinational", "MUX", 16),
    ("74147", "Decimal-to-BCD Encoder", "Combinational", "ENCODER", 16),
    ("7483", "4-bit Binary Adder", "Arithmetic", "ADDER", 16),
    ("74193", "4-bit Up/Down Counter", "Sequential Logic", "COUNTER", 16),
    ("555", "Timer IC", "Analog / Timer", "ANALOG", 8),
    ("LM358", "Dual Operational Amplifier", "Analog Electronics", "ANALOG", 8),
    ("LM741", "Operational Amplifier", "Analog Electronics", "ANALOG", 8),
    ("LM324", "Quad Operational Amplifier", "Analog Electronics", "ANALOG", 14),
    ("LM386", "Audio Power Amplifier", "Analog Electronics", "ANALOG", 8),
    ("7805", "5V Voltage Regulator", "Power Electronics", "POWER", 3),
    ("7812", "12V Voltage Regulator", "Power Electronics", "POWER", 3),
    ("7809", "9V Voltage Regulator", "Power Electronics", "POWER", 3),
    ("ADC0804", "8-bit Analog-to-Digital Converter", "Data Conversion", "ADC", 20),
    ("DAC0808", "8-bit Digital-to-Analog Converter", "Data Conversion", "DAC", 16),
    ("ATmega328P", "AVR Microcontroller", "Microcontrollers", "MCU", 28),
    ("NE5532", "Dual Low-Noise Op-Amp", "Analog Electronics", "ANALOG", 8),
]

SUBJECTS = {
    "Digital Electronics": [
        "Number systems and Boolean algebra",
        "Logic gates and truth tables",
        "Karnaugh maps",
        "Combinational circuits",
        "Multiplexers and decoders",
        "Flip-flops, counters and registers",
    ],
    "Analog Electronics": [
        "Diodes and rectifiers",
        "BJT and MOSFET basics",
        "Amplifiers and biasing",
        "Operational amplifiers",
        "Oscillators and feedback",
    ],
    "Network Theory": [
        "Ohm's law, KCL and KVL",
        "Thevenin and Norton theorems",
        "Mesh and nodal analysis",
        "RC and RL circuits",
        "AC circuit analysis",
    ],
    "Microprocessors": [
        "Processor architecture",
        "Registers and instruction sets",
        "Memory interfacing",
        "Input/output interfacing",
        "Interrupts and buses",
    ],
    "Embedded Systems": [
        "Microcontroller architecture",
        "GPIO and digital interfaces",
        "Timers and interrupts",
        "UART, SPI and I2C",
        "Sensor interfacing",
    ],
    "VLSI Design": [
        "CMOS logic fundamentals",
        "Digital circuit design",
        "Verilog HDL",
        "RTL design and verification",
        "Synthesis and timing concepts",
    ],
    "Communication Systems": [
        "Amplitude modulation",
        "Frequency modulation",
        "Sampling and quantization",
        "Digital modulation",
        "Noise and bandwidth",
    ],
    "Signals and Systems": [
        "Continuous and discrete signals",
        "Linear time-invariant systems",
        "Convolution",
        "Fourier series and transforms",
        "Laplace transforms",
    ],
    "Control Systems": [
        "Transfer functions",
        "Block diagrams",
        "Stability analysis",
        "Root locus",
        "Frequency response",
    ],
    "Verilog HDL": [
        "Modules and ports",
        "Continuous assignments",
        "Combinational always blocks",
        "Sequential logic",
        "Testbenches and simulation",
    ],
}


PIN_LABELS = {
    "7400": ["1A", "1B", "1Y", "2A", "2B", "2Y", "GND",
             "3Y", "3A", "3B", "4Y", "4A", "4B", "VCC"],
    "7402": ["1Y", "1A", "1B", "2Y", "2A", "2B", "GND",
             "3A", "3B", "3Y", "4A", "4B", "4Y", "VCC"],
    "7404": ["1A", "1Y", "2A", "2Y", "3A", "3Y", "GND",
             "4Y", "4A", "5Y", "5A", "6Y", "6A", "VCC"],
    "7408": ["1A", "1B", "1Y", "2A", "2B", "2Y", "GND",
             "3Y", "3A", "3B", "4Y", "4A", "4B", "VCC"],
    "7432": ["1A", "1B", "1Y", "2A", "2B", "2Y", "GND",
             "3Y", "3A", "3B", "4Y", "4A", "4B", "VCC"],
    "7486": ["1A", "1B", "1Y", "2A", "2B", "2Y", "GND",
             "3Y", "3A", "3B", "4Y", "4A", "4B", "VCC"],
}


def gate_value(gate, a, b=False):
    """Return a binary output for a supported logic gate."""
    a, b = int(bool(a)), int(bool(b))

    if gate == "AND":
        return a & b
    if gate == "OR":
        return a | b
    if gate == "NAND":
        return 1 - (a & b)
    if gate == "NOR":
        return 1 - (a | b)
    if gate == "XOR":
        return a ^ b
    if gate == "XNOR":
        return 1 - (a ^ b)
    if gate == "NOT":
        return 1 - a

    return 0


class OpenElectronicsLab:
    def __init__(self, root):
        self.root = root
        self.root.title("Open Electronics Lab | Virtual Engineering Lab")
        self.root.geometry("1280x820")
        self.root.minsize(900, 650)
        self.root.configure(bg=BG)

        self.switches = [False, False, False, False]
        self.selected_ic = "7400"
        self.wires = []
        self.current_page = "Dashboard"
        self.page_buttons = {}
        self.ic_widgets = []

        self.configure_styles()
        self.build_layout()
        self.show_page("Dashboard")

    # --------------------------------------------------------
    # STYLE
    # --------------------------------------------------------

    def configure_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Dark.TCombobox",
            fieldbackground=PANEL2,
            background=PANEL2,
            foreground=TEXT,
            arrowcolor=CYAN,
        )

        style.map(
            "Dark.TCombobox",
            fieldbackground=[("readonly", PANEL2)],
            foreground=[("readonly", TEXT)],
        )

    def make_button(self, parent, text, command,
                    color=CYAN, background=PANEL2):
        return tk.Button(
            parent,
            text=text,
            command=command,
            bg=background,
            fg=color,
            activebackground="#203b52",
            activeforeground=TEXT,
            relief="flat",
            bd=0,
            padx=12,
            pady=9,
            cursor="hand2",
            font=("Segoe UI", 10),
        )

    def make_card(self, parent, title=None):
        card = tk.Frame(
            parent,
            bg=PANEL,
            highlightbackground=BORDER,
            highlightthickness=1,
            padx=15,
            pady=15,
        )
        if title:
            tk.Label(
                card,
                text=title,
                bg=PANEL,
                fg=TEXT,
                font=("Segoe UI", 12, "bold"),
            ).pack(anchor="w", pady=(0, 12))
        return card

    def make_label(self, parent, text, size=10, color=TEXT, bold=False):
        return tk.Label(
            parent,
            text=text,
            bg=parent.cget("bg"),
            fg=color,
            font=("Segoe UI", size, "bold" if bold else "normal"),
            justify="left",
            anchor="w",
            wraplength=650,
        )

    # --------------------------------------------------------
    # MAIN WINDOW
    # --------------------------------------------------------

    def build_layout(self):
        self.sidebar = tk.Frame(self.root, bg=SIDEBAR, width=225)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        self.content = tk.Frame(self.root, bg=BG)
        self.content.pack(side="right", fill="both", expand=True)

        brand = tk.Frame(self.sidebar, bg=SIDEBAR, padx=15, pady=23)
        brand.pack(fill="x")

        tk.Label(
            brand, text="⌘", bg="#143349", fg=CYAN,
            font=("Segoe UI", 23, "bold"), padx=10, pady=4
        ).pack(side="left", padx=(0, 9))

        tk.Label(
            brand, text="OPEN ELECTRONICS\nVirtual Engineering Lab",
            bg=SIDEBAR, fg=TEXT, justify="left",
            font=("Segoe UI", 11, "bold")
        ).pack(side="left")

        groups = {
            "WORKSPACE": [
                "Dashboard", "IC Trainer Kit", "Circuit Connections",
                "Logic Gate Lab", "Truth Tables"
            ],
            "LEARNING": [
                "IC Library", "ECE Subjects", "Lab Information"
            ]
        }

        for group, pages in groups.items():
            tk.Label(
                self.sidebar, text=group, bg=SIDEBAR, fg=MUTED,
                font=("Segoe UI", 9, "bold"), padx=15, pady=10
            ).pack(anchor="w")

            for page in pages:
                button = tk.Button(
                    self.sidebar,
                    text="  ◈   " + page,
                    command=lambda p=page: self.show_page(p),
                    bg=SIDEBAR,
                    fg=MUTED,
                    activebackground="#193047",
                    activeforeground=CYAN,
                    relief="flat",
                    bd=0,
                    anchor="w",
                    padx=12,
                    pady=12,
                    cursor="hand2",
                    font=("Segoe UI", 10),
                )
                button.pack(fill="x", padx=7, pady=1)
                self.page_buttons[page] = button

        self.topbar = tk.Frame(
            self.content, bg=BG, padx=24, pady=19
        )
        self.topbar.pack(fill="x")

        self.title_label = tk.Label(
            self.topbar, text="", bg=BG, fg=TEXT,
            font=("Segoe UI", 21, "bold")
        )
        self.title_label.pack(side="left")

        tk.Label(
            self.topbar, text="● SIMULATOR READY",
            bg="#103025", fg=GREEN,
            font=("Segoe UI", 9, "bold"), padx=10, pady=7
        ).pack(side="right")

        self.subtitle = tk.Label(
            self.content, text="Learn, connect and experiment.",
            bg=BG, fg=MUTED, font=("Segoe UI", 10),
            anchor="w", padx=24
        )
        self.subtitle.pack(fill="x", pady=(0, 12))

        self.page_area = tk.Frame(self.content, bg=BG)
        self.page_area.pack(fill="both", expand=True, padx=24, pady=(0, 20))

    def clear_page(self):
        for widget in self.page_area.winfo_children():
            widget.destroy()

    def show_page(self, page):
        self.current_page = page
        self.clear_page()

        self.title_label.config(text=page)

        subtitles = {
            "Dashboard": "Your electronics engineering workspace.",
            "IC Trainer Kit": "Switches, IC pins, LEDs and digital experiments.",
            "Circuit Connections": "Create and inspect virtual jumper connections.",
            "Logic Gate Lab": "Test the seven fundamental logic gates.",
            "Truth Tables": "Generate truth tables for Boolean functions.",
            "IC Library": "Browse common integrated circuits.",
            "ECE Subjects": "Explore electronics and communication engineering.",
            "Lab Information": "Features, limitations and instructions.",
        }
        self.subtitle.config(text=subtitles.get(page, ""))

        for name, button in self.page_buttons.items():
            button.config(
                bg="#193047" if name == page else SIDEBAR,
                fg=CYAN if name == page else MUTED
            )

        pages = {
            "Dashboard": self.page_dashboard,
            "IC Trainer Kit": self.page_trainer,
            "Circuit Connections": self.page_connections,
            "Logic Gate Lab": self.page_logic,
            "Truth Tables": self.page_truth,
            "IC Library": self.page_library,
            "ECE Subjects": self.page_subjects,
            "Lab Information": self.page_information,
        }
        pages[page]()

    # --------------------------------------------------------
    # DASHBOARD
    # --------------------------------------------------------

    def page_dashboard(self):
        self.make_label(
            self.page_area,
            "Welcome to your electronics laboratory.",
            18, CYAN, True
        ).pack(anchor="w", pady=(4, 8))

        self.make_label(
            self.page_area,
            "Experiment with digital logic, ICs, binary switches and output indicators.",
            10, MUTED
        ).pack(anchor="w", pady=(0, 20))

        stats = tk.Frame(self.page_area, bg=BG)
        stats.pack(fill="x", pady=(0, 18))

        values = [
            (str(len(IC_DATABASE)), "IC CATALOGUE"),
            ("7", "LOGIC FUNCTIONS"),
            ("4", "INPUT SWITCHES"),
            ("14+", "ECE TOPICS"),
        ]

        for value, label in values:
            card = self.make_card(stats)
            card.pack(side="left", fill="both", expand=True, padx=(0, 9))
            tk.Label(
                card, text=value, bg=PANEL, fg=CYAN,
                font=("Segoe UI", 22, "bold")
            ).pack(anchor="w")
            tk.Label(
                card, text=label, bg=PANEL, fg=MUTED,
                font=("Segoe UI", 9)
            ).pack(anchor="w", pady=(5, 0))

        card = self.make_card(self.page_area, "QUICK EXPERIMENTS")
        card.pack(fill="x", pady=(0, 14))

        for number, ic, description in [
            ("01", "7400", "Build a NAND gate experiment"),
            ("02", "7408", "Explore AND gate behaviour"),
            ("03", "7432", "Test an OR gate"),
            ("04", "7486", "Understand XOR logic"),
        ]:
            row = tk.Frame(card, bg=PANEL)
            row.pack(fill="x", pady=4)
            tk.Label(
                row, text=number, bg=PANEL, fg=CYAN,
                font=("Segoe UI", 12, "bold"), width=4
            ).pack(side="left")
            tk.Label(
                row, text=description, bg=PANEL, fg=TEXT
            ).pack(side="left", padx=10)
            self.make_button(
                row, "Open", lambda n=ic: self.open_ic(n)
            ).pack(side="right")

        info = self.make_card(self.page_area, "IMPORTANT")
        info.pack(fill="x")
        self.make_label(
            info,
            "This application simulates selected digital logic. "
            "It is not a full electrical simulator and does not yet model "
            "analog waveforms, real electrical current, propagation delays "
            "or all functions of every IC.",
            10, YELLOW
        ).pack(anchor="w")

    # --------------------------------------------------------
    # VIRTUAL TRAINER KIT
    # --------------------------------------------------------

    def toggle_switch(self, index):
        self.switches[index] = not self.switches[index]
        self.show_page("IC Trainer Kit")

    def selected_ic_info(self):
        for item in IC_DATABASE:
            if item[0] == self.selected_ic:
                return item
        return IC_DATABASE[0]

    def output_value(self):
        ic = self.selected_ic_info()
        gate = ic[3]
        return gate_value(gate, self.switches[0], self.switches[1])

    def render_switches(self, parent):
        frame = tk.Frame(parent, bg=PANEL)
        frame.pack(fill="x", pady=5)

        for i, state in enumerate(self.switches):
            color = GREEN if state else MUTED
            text = "ON  /  1" if state else "OFF / 0"

            button = tk.Button(
                frame,
                text=f"SWITCH {'ABCD'[i]}\n\n{text}",
                command=lambda j=i: self.toggle_switch(j),
                bg="#124b3b" if state else PANEL2,
                fg=color,
                activebackground="#203b52",
                activeforeground=TEXT,
                relief="flat",
                padx=8,
                pady=12,
                font=("Segoe UI", 10, "bold"),
                cursor="hand2",
            )
            button.pack(side="left", fill="x", expand=True, padx=4)

    def render_leds(self, parent):
        frame = tk.Frame(parent, bg=PANEL)
        frame.pack(fill="x", pady=8)

        output = self.output_value()

        for i in range(4):
            active = output if i == 0 else (
                int(self.switches[i - 1]) if i > 0 else 0
            )

            cell = tk.Frame(frame, bg=PANEL2, padx=10, pady=10)
            cell.pack(side="left", fill="x", expand=True, padx=4)

            canvas = tk.Canvas(
                cell, width=42, height=42,
                bg=PANEL2, highlightthickness=0
            )
            canvas.pack()

            color = GREEN if active else "#293644"
            canvas.create_oval(
                8, 8, 34, 34,
                fill=color, outline=GREEN if active else "#526174",
                width=2
            )

            tk.Label(
                cell, text=f"LED {i + 1}",
                bg=PANEL2, fg=TEXT,
                font=("Segoe UI", 9)
            ).pack()

            tk.Label(
                cell, text=f"OUTPUT {active}",
                bg=PANEL2, fg=GREEN if active else MUTED,
                font=("Segoe UI", 8)
            ).pack()

    def page_trainer(self):
        top = self.make_card(self.page_area, "DIGITAL TRAINER BOARD")
        top.pack(fill="x", pady=(0, 14))

        self.render_switches(top)

        tk.Label(
            top, text="INPUT SWITCHES  |  OFF = 0  |  ON = 1",
            bg=PANEL, fg=MUTED, font=("Segoe UI", 9)
        ).pack(anchor="w", pady=(8, 0))

        bottom = tk.Frame(self.page_area, bg=BG)
        bottom.pack(fill="both", expand=True)

        left = self.make_card(bottom, "IC SELECTION")
        left.pack(side="left", fill="both", expand=True, padx=(0, 8))

        self.ic_var = tk.StringVar(value=self.selected_ic)
        combo = ttk.Combobox(
            left,
            textvariable=self.ic_var,
            values=[f"{x[0]} — {x[1]}" for x in IC_DATABASE],
            state="readonly",
            width=35,
        )
        combo.pack(fill="x", pady=5)
        combo.bind("<<ComboboxSelected>>", self.change_ic)

        ic = self.selected_ic_info()

        tk.Label(
            left, text=f"IC {ic[0]}",
            bg=PANEL, fg=CYAN,
            font=("Consolas", 23, "bold")
        ).pack(anchor="w", pady=(18, 5))

        tk.Label(
            left, text=ic[1], bg=PANEL, fg=TEXT,
            font=("Segoe UI", 12, "bold")
        ).pack(anchor="w")

        tk.Label(
            left, text=f"Category: {ic[2]}\nLogic model: {ic[3]}\nNominal package pins: {ic[4]}",
            bg=PANEL, fg=MUTED,
            justify="left", font=("Segoe UI", 10)
        ).pack(anchor="w", pady=12)

        tk.Label(
            left,
            text="This demo evaluates the first supported logic function "
                 "using switches A and B. It does not simulate every gate "
                 "or internal function inside a multi-gate IC.",
            bg=PANEL, fg=YELLOW, wraplength=380,
            justify="left", font=("Segoe UI", 9)
        ).pack(anchor="w", pady=5)

        right = self.make_card(bottom, "OUTPUT INDICATORS")
        right.pack(side="left", fill="both", expand=True, padx=(8, 0))

        self.render_leds(right)

        tk.Label(
            right,
            text=f"Input A = {int(self.switches[0])}\n"
                 f"Input B = {int(self.switches[1])}\n"
                 f"Modelled output = {self.output_value()}",
            bg=PANEL, fg=GREEN,
            font=("Consolas", 12), justify="left"
        ).pack(anchor="w", pady=15)

        tk.Label(
            right,
            text="Pin layout",
            bg=PANEL, fg=TEXT,
            font=("Segoe UI", 12, "bold")
        ).pack(anchor="w", pady=(8, 4))

        pins = PIN_LABELS.get(self.selected_ic)

        if pins:
            grid = tk.Frame(right, bg=PANEL)
            grid.pack(anchor="w", fill="x")

            for i, name in enumerate(pins):
                color = GREEN if name in ("VCC", "GND") else CYAN
                tk.Label(
                    grid,
                    text=f"{i + 1}: {name}",
                    bg=PANEL2, fg=color,
                    font=("Consolas", 8),
                    padx=5, pady=5,
                    width=8
                ).grid(row=i // 4, column=i % 4, padx=2, pady=2)
        else:
            tk.Label(
                right,
                text="Pin labels are not included for this IC yet. "
                     "Consult the exact manufacturer's datasheet.",
                bg=PANEL, fg=YELLOW, wraplength=350,
                justify="left"
            ).pack(anchor="w")

    def change_ic(self, event=None):
        value = self.ic_var.get().split(" — ")[0]
        self.selected_ic = value
        self.show_page("IC Trainer Kit")

    def open_ic(self, number):
        self.selected_ic = number
        self.show_page("IC Trainer Kit")

    # --------------------------------------------------------
    # CIRCUIT CONNECTIONS
    # --------------------------------------------------------

    def page_connections(self):
        card = self.make_card(self.page_area, "VIRTUAL JUMPER CONNECTIONS")
        card.pack(fill="x", pady=(0, 14))

        tk.Label(
            card,
            text="Choose a source and destination to add a visual connection.",
            bg=PANEL, fg=MUTED
        ).pack(anchor="w", pady=(0, 12))

        row = tk.Frame(card, bg=PANEL)
        row.pack(fill="x")

        self.source_var = tk.StringVar(value="Switch A")
        self.target_var = tk.StringVar(value="LED 1")

        tk.Label(row, text="Source", bg=PANEL, fg=TEXT).pack(anchor="w")
        ttk.Combobox(
            row, textvariable=self.source_var, state="readonly",
            values=["Switch A", "Switch B", "Switch C", "Switch D",
                    "+5V supply", "Ground"],
            width=22
        ).pack(anchor="w", pady=(3, 12))

        tk.Label(row, text="Destination", bg=PANEL, fg=TEXT).pack(anchor="w")
        destinations = [
            "LED 1", "LED 2", "LED 3", "LED 4"
        ] + [
            f"IC Pin {i}" for i in range(
                1, self.selected_ic_info()[4] + 1
            )
        ]

        ttk.Combobox(
            row, textvariable=self.target_var,
            values=destinations, state="readonly", width=22
        ).pack(anchor="w", pady=(3, 12))

        self.make_button(
            row, "+ Add connection", self.add_wire
        ).pack(anchor="w")

        warning = self.make_card(
            self.page_area, "CONNECTION SAFETY"
        )
        warning.pack(fill="x", pady=(0, 14))

        tk.Label(
            warning,
            text="This is a visual connection list only. It does not "
                 "solve electrical nets, detect shorts, check IC voltage "
                 "compatibility or calculate real current.",
            bg=PANEL, fg=YELLOW, wraplength=700,
            justify="left"
        ).pack(anchor="w")

        self.wire_card = self.make_card(
            self.page_area, "YOUR CONNECTIONS"
        )
        self.wire_card.pack(fill="both", expand=True)
        self.render_wires()

    def add_wire(self):
        source = self.source_var.get()
        target = self.target_var.get()

        if any(w[0] == source and w[1] == target for w in self.wires):
            messagebox.showinfo("Connection", "This connection already exists.")
            return

        self.wires.append((source, target))
        self.show_page("Circuit Connections")

    def remove_wire(self, index):
        if 0 <= index < len(self.wires):
            self.wires.pop(index)
        self.show_page("Circuit Connections")

    def render_wires(self):
        if not hasattr(self, "wire_card"):
            return

        for widget in self.wire_card.winfo_children():
            widget.destroy()

        if not self.wires:
            tk.Label(
                self.wire_card,
                text="No connections yet. Add a jumper connection above.",
                bg=PANEL, fg=MUTED
            ).pack(anchor="w")
            return

        for index, (source, target) in enumerate(self.wires):
            row = tk.Frame(self.wire_card, bg=PANEL)
            row.pack(fill="x", pady=4)

            tk.Label(
                row, text=f"{source}  ━━━→  {target}",
                bg=PANEL, fg=CYAN,
                font=("Consolas", 10)
            ).pack(side="left")

            self.make_button(
                row, "Remove",
                lambda i=index: self.remove_wire(i),
                color=RED
            ).pack(side="right")

        self.make_button(
            self.wire_card, "Clear all connections",
            self.clear_wires, color=RED
        ).pack(anchor="w", pady=(12, 0))

    def clear_wires(self):
        self.wires.clear()
        self.show_page("Circuit Connections")

    # --------------------------------------------------------
    # LOGIC GATE LAB
    # --------------------------------------------------------

    def page_logic(self):
        card = self.make_card(self.page_area, "INTERACTIVE INPUTS")
        card.pack(fill="x", pady=(0, 14))

        self.gate_a = tk.BooleanVar(value=self.switches[0])
        self.gate_b = tk.BooleanVar(value=self.switches[1])

        row = tk.Frame(card, bg=PANEL)
        row.pack(anchor="w")

        tk.Checkbutton(
            row, text="Input A = 1",
            variable=self.gate_a, command=self.update_logic,
            bg=PANEL, fg=CYAN, selectcolor=PANEL2,
            activebackground=PANEL, activeforeground=TEXT
        ).pack(side="left", padx=10)

        tk.Checkbutton(
            row, text="Input B = 1",
            variable=self.gate_b, command=self.update_logic,
            bg=PANEL, fg=CYAN, selectcolor=PANEL2,
            activebackground=PANEL, activeforeground=TEXT
        ).pack(side="left", padx=10)

        self.gate_results = self.make_card(
            self.page_area, "LIVE GATE OUTPUTS"
        )
        self.gate_results.pack(fill="both", expand=True)

        self.update_logic()

    def update_logic(self):
        if not hasattr(self, "gate_results"):
            return

        for widget in self.gate_results.winfo_children():
            widget.destroy()

        a = self.gate_a.get()
        b = self.gate_b.get()

        expressions = [
            ("AND", "A · B"),
            ("OR", "A + B"),
            ("NOT", "A′"),
            ("NAND", "(A · B)′"),
            ("NOR", "(A + B)′"),
            ("XOR", "A ⊕ B"),
            ("XNOR", "(A ⊕ B)′"),
        ]

        for gate, expression in expressions:
            output = gate_value(gate, a, b)
            row = tk.Frame(self.gate_results, bg=PANEL2, padx=12, pady=9)
            row.pack(fill="x", pady=4)

            tk.Label(
                row, text=gate, width=9,
                bg=PANEL2, fg=CYAN,
                font=("Segoe UI", 11, "bold")
            ).pack(side="left")

            tk.Label(
                row, text=expression, bg=PANEL2, fg=TEXT,
                font=("Consolas", 12)
            ).pack(side="left", padx=10)

            tk.Label(
                row, text=f"OUTPUT = {output}",
                bg=PANEL2, fg=GREEN if output else MUTED,
                font=("Consolas", 11, "bold")
            ).pack(side="right")

    # --------------------------------------------------------
    # TRUTH TABLES
    # --------------------------------------------------------

    def page_truth(self):
        card = self.make_card(self.page_area, "TRUTH TABLE GENERATOR")
        card.pack(fill="x", pady=(0, 14))

        self.truth_var = tk.StringVar(value="NAND")

        tk.Label(
            card, text="Select logic function:",
            bg=PANEL, fg=TEXT
        ).pack(anchor="w")

        ttk.Combobox(
            card, textvariable=self.truth_var,
            values=["AND", "OR", "NOT", "NAND", "NOR", "XOR", "XNOR"],
            state="readonly", width=20
        ).pack(anchor="w", pady=8)

        self.make_button(
            card, "Generate truth table", self.generate_truth
        ).pack(anchor="w")

        self.truth_result = self.make_card(
            self.page_area, "RESULT"
        )
        self.truth_result.pack(fill="both", expand=True)

        self.generate_truth()

    def generate_truth(self):
        if not hasattr(self, "truth_result"):
            return

        for widget in self.truth_result.winfo_children():
            widget.destroy()

        gate = self.truth_var.get()

        if gate == "NOT":
            rows = [(0, None), (1, None)]
        else:
            rows = [(0, 0), (0, 1), (1, 0), (1, 1)]

        headers = ["A", "Output"] if gate == "NOT" else ["A", "B", "Output"]

        table = tk.Frame(self.truth_result, bg=PANEL)
        table.pack(anchor="nw", fill="x")

        for column, heading in enumerate(headers):
            tk.Label(
                table, text=heading, bg="#18334a", fg=CYAN,
                font=("Segoe UI", 10, "bold"),
                padx=22, pady=10
            ).grid(row=0, column=column, sticky="ew", padx=1, pady=1)

        for row_number, (a, b) in enumerate(rows, start=1):
            output = gate_value(gate, a, b if b is not None else False)

            values = [a, output] if gate == "NOT" else [a, b, output]

            for column, value in enumerate(values):
                tk.Label(
                    table, text=str(value),
                    bg=PANEL2 if row_number % 2 else PANEL,
                    fg=GREEN if column == len(values) - 1 else TEXT,
                    font=("Consolas", 11),
                    padx=22, pady=10
                ).grid(row=row_number, column=column, sticky="ew",
                       padx=1, pady=1)

        tk.Label(
            self.truth_result,
            text=f"Boolean function: {gate}",
            bg=PANEL, fg=MUTED,
            font=("Segoe UI", 10)
        ).pack(anchor="w", pady=15)

    # --------------------------------------------------------
    # IC LIBRARY
    # --------------------------------------------------------

    def page_library(self):
        search_card = self.make_card(self.page_area, "SEARCH IC CATALOGUE")
        search_card.pack(fill="x", pady=(0, 12))

        self.search_var = tk.StringVar()

        entry = tk.Entry(
            search_card, textvariable=self.search_var,
            bg=PANEL2, fg=TEXT, insertbackground=TEXT,
            relief="flat", font=("Segoe UI", 11)
        )
        entry.pack(fill="x", ipady=8)
        entry.insert(0, "")

        self.ic_results = tk.Frame(self.page_area, bg=BG)
        self.ic_results.pack(fill="both", expand=True)

        self.search_var.trace_add(
            "write", lambda *_: self.render_ic_library()
        )

        self.render_ic_library()

    def render_ic_library(self):
        if not hasattr(self, "ic_results"):
            return

        for widget in self.ic_results.winfo_children():
            widget.destroy()

        query = self.search_var.get().lower().strip()

        matches = [
            ic for ic in IC_DATABASE
            if query in " ".join(map(str, ic)).lower()
        ]

        if not matches:
            tk.Label(
                self.ic_results,
                text="No matching IC found.",
                bg=BG, fg=MUTED
            ).pack(anchor="w")
            return

        for ic in matches:
            number, name, category, gate, pins = ic

            card = self.make_card(self.ic_results)
            card.pack(fill="x", pady=4)

            row = tk.Frame(card, bg=PANEL)
            row.pack(fill="x")

            tk.Label(
                row, text=number, bg=PANEL, fg=CYAN,
                font=("Consolas", 17, "bold"), width=12,
                anchor="w"
            ).pack(side="left")

            details = tk.Frame(row, bg=PANEL)
            details.pack(side="left", fill="x", expand=True)

            tk.Label(
                details, text=name, bg=PANEL, fg=TEXT,
                font=("Segoe UI", 10, "bold")
            ).pack(anchor="w")

            tk.Label(
                details,
                text=f"{category}  |  Model: {gate}  |  Package pins: {pins}",
                bg=PANEL, fg=MUTED,
                font=("Segoe UI", 9)
            ).pack(anchor="w", pady=(3, 0))

            self.make_button(
                row, "Open in trainer",
                lambda n=number: self.open_ic(n)
            ).pack(side="right")

    # --------------------------------------------------------
    # ECE SUBJECTS
    # --------------------------------------------------------

    def page_subjects(self):
        tk.Label(
            self.page_area,
            text="ELECTRONICS & COMMUNICATION ENGINEERING",
            bg=BG, fg=CYAN,
            font=("Segoe UI", 14, "bold")
        ).pack(anchor="w", pady=(0, 12))

        canvas = tk.Canvas(
            self.page_area, bg=BG, highlightthickness=0
        )
        scrollbar = ttk.Scrollbar(
            self.page_area, orient="vertical", command=canvas.yview
        )
        scroll_frame = tk.Frame(canvas, bg=BG)

        scroll_frame.bind(
            "<Configure>",
            lambda event: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window(
            (0, 0), window=scroll_frame, anchor="nw"
        )
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for subject, topics in SUBJECTS.items():
            card = self.make_card(scroll_frame, subject)
            card.pack(fill="x", pady=5, padx=(0, 10))

            for topic in topics:
                tk.Label(
                    card,
                    text="•  " + topic,
                    bg=PANEL, fg=MUTED,
                    font=("Segoe UI", 10)
                ).pack(anchor="w", pady=3)

    # --------------------------------------------------------
    # INFORMATION
    # --------------------------------------------------------

    def page_information(self):
        card = self.make_card(self.page_area, "ABOUT THIS APPLICATION")
        card.pack(fill="x", pady=(0, 14))

        sections = [
            (
                "Current features",
                "Virtual binary switches, LED indicators, selected digital "
                "logic functions, truth tables, an IC catalogue, pin layouts, "
                "visual jumper connections and ECE learning topics."
            ),
            (
                "Important limitation",
                "The IC catalogue is educational. Selecting an IC does not "
                "implement every internal gate, counter, amplifier or "
                "converter in that device. Pin layouts are included only "
                "for selected ICs and must be checked against datasheets."
            ),
            (
                "Not yet implemented",
                "Analog circuit simulation, real voltage and current, "
                "oscilloscope waveforms, transistor-level SPICE, timing "
                "analysis, complete circuit-net solving, Verilog execution "
                "and microcontroller firmware emulation."
            ),
            (
                "How to run",
                "Save this program as open_electronics_lab.py. Run it using "
                "python open_electronics_lab.py in the VS Code terminal. "
                "Python's Tkinter is included with many standard Python "
                "installations."
            ),
        ]

        for heading, description in sections:
            tk.Label(
                card, text=heading,
                bg=PANEL, fg=CYAN,
                font=("Segoe UI", 12, "bold")
            ).pack(anchor="w", pady=(10, 5))

            tk.Label(
                card, text=description,
                bg=PANEL, fg=MUTED,
                font=("Segoe UI", 10),
                wraplength=800, justify="left"
            ).pack(anchor="w", pady=(0, 7))


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = OpenElectronicsLab(root)
    root.mainloop()
