# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import extension
from os import system

   
mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(['mod4'], 'r', lazy.run_extension(extension.J4DmenuDesktop(
        dmenu_prompt=">",
        dmenu_font="Andika-8",
        background="#15181a",
        foreground="#00ff00",
        selected_background="#079822",
        selected_foreground="#fff",
        dmenu_ignorecase=True,
        dmenu_lines=20,
        j4dmenu_display_binary=True,
        j4dmenu_terminal="alacritty",
       # dmenu_height=24,  # Only supported by some dmenu forks
    ))),
    Key([mod], "e",  lazy.run_extension(
        extension.CommandSet(
            commands={
             'lock': '/home/Jlisowskyy/.local/bin/lock.sh',
              'shut': 'shutdown now',
              'reb': 'reboot',
                'sus': 'systemctl suspend',
            },
            dmenu_prompt=">",
            dmenu_ignorecase=True,
    ))),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# // ------------------------------
# // ScratchPads
# // ------------------------------

groups.append(ScratchPad('scratchpad',[
    DropDown('mixer', 'pavucontrol'),
    DropDown('bitwarden', 'bitwarden-desktop'),
    DropDown('nnn', 'alacritty -e nnn -d -C', x=0.3, y=0.15, width=0.4, height=0.7),
    DropDown('term', 'alacritty'),
    DropDown('plan', 'feh /home/Jlisowskyy/Zajecia/plan.png', x=0.35, y=0.2, width=0.3, height=0.6),
]))

keys.extend([
    Key(["control"], "1", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key(["control"], "2", lazy.group['scratchpad'].dropdown_toggle('plan')),
    Key(["control"], "3", lazy.group['scratchpad'].dropdown_toggle('nnn')),
    Key(["control"], "4", lazy.group['scratchpad'].dropdown_toggle('bitwarden')),
    Key(["control"], "5", lazy.group['scratchpad'].dropdown_toggle('mixer')),
])

# // ------------------------------
# // layouts
# // ------------------------------



layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    layout.MonadTall(),
    layout.RatioTile(),
    layout.Tile(),
    layout.floating.Floating(),
]

widget_defaults = dict(
    font="terminus",
    fontsize=14,
    padding=3,
)

extension_defaults = widget_defaults.copy()
wallpaper_dir = "/home/Jlisowskyy/Wallpapers/"


screens = [
        # 1k Screen reso
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
            ],
            32,
	    ),
        top=bar.Bar([
		        widget.CPU(),
                widget.Sep(linewidth=4),
                widget.ThermalSensor(format='CPU Package: {temp:.0f}{unit}', tag_sensor="Package id 0"),
                widget.Sep(linewidth=4),
                widget.Memory(),
                widget.Sep(linewidth=4),
                widget.Net(), 
                widget.Sep(linewidth=4),
                widget.CapsNumLockIndicator(),
                widget.Sep(linewidth=4),
                widget.PulseVolume(volume_app="pavucontrol", fmt="Vol: {}"),
            ],
            16,
        ),
        wallpaper=wallpaper_dir + "w1k.jpg",
    ),

    # 2k resolutions screen
	Screen(
	bottom=bar.Bar(
		[
			widget.CurrentLayout(),
			widget.GroupBox(),
			widget.Prompt(),
			widget.WindowName(),
			# NB Systray is incompatible with Wayland, consider using StatusNotifier instead
			widget.StatusNotifier(),
			widget.Systray(),
			widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
		],
		32,
	),
	top=bar.Bar([
			widget.CPU(),
			widget.Sep(linewidth=4),
			widget.ThermalSensor(format='CPU Package: {temp:.0f}{unit}', tag_sensor="Package id 0"),
			widget.Sep(linewidth=4),
			widget.Memory(),
			widget.Sep(linewidth=4),
			widget.Net(), 
			widget.Sep(linewidth=4),
			widget.CapsNumLockIndicator(),
			widget.Sep(linewidth=4),
			widget.PulseVolume(volume_app="pavucontrol", fmt="Vol: {}"),
		],
		24,
	),
	wallpaper=wallpaper_dir + "w2k.jpg"
    ),


]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
wmname = "Qtile" #LG3D  

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None 
