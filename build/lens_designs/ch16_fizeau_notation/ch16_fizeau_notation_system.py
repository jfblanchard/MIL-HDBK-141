"""Fig 16.2: notation with respect to the Fizeau interferoscope or interferometer.

Construction schematic at the scan's own layout (drawing units = scan pixels / 100 on a 1/1.7 preview of ch16 p4, y up):
pinhole H at the focus of the collimating lens L1, beam splitter turning the returning light to L2 and the image plane,
optical flat S1 over the inclined surface S2 (wedge angle alpha, exaggerated), and the X, Z, P frame at O."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403
from matplotlib.patches import Polygon  # noqa: E402

Q = lambda x, y: P(x / 100, -y / 100)
fig, ax = canvas(4.6, (0.2, 15.6), (-19.4, -0.4))
xa, ya = 6.03, -17.05                                   # optical axis column and the X axis (S1)
H, C, A, B, O = Q(603, 373), Q(400, 1705), Q(603, 1705), Q(603, 1785), Q(1487, 1705)
l1_y = -14.33
# pinhole screen with the hole on the axis
for x0, x1 in ((3.9, 5.97), (6.09, 8.3)):
    line(ax, P(x0, H[1]), P(x1, H[1]), color=INK, linewidth=2.2, solid_capstyle="butt")
# beam splitter (a line in the scan)
line(ax, Q(393, 818), Q(760, 490), color=INK, linewidth=0.9, solid_capstyle="butt", zorder=3)
# lenses as ideal thin lenses: L1 horizontal, L2 vertical
tlens(ax, P(5.425, l1_y), 3.575, 0)
tlens(ax, Q(895, 630), 1.7, 90)
# image plane
line(ax, Q(1108, 470), Q(1108, 775), color=INK, linewidth=0.9, solid_capstyle="butt")
# plates: upper flat (S1 its lower face, on the X axis), lower block inclined (S2 its upper face)
ax.add_patch(plt.Rectangle((2.50, ya), 6.0, 1.07, **{**MEDIUM, "fill": False}))
ax.add_patch(Polygon([Q(252, 1820), Q(855, 1762), Q(860, 1855), Q(262, 1915)], closed=True, **{**MEDIUM, "fill": False}))
# rays: the axial ray H -> A and back, the oblique ray through C, the reflected rays at angle theta
ray(ax, [H, A], AXIAL, arrows=())
for y, d in ((-9.95, -1), (-11.35, 1), (-16.15, -1), (-16.90, 1)):
    head(ax, P(xa, y), P(0, d), AXIAL)
line(ax, Q(603, 65), H, **AXIAL)
top = Q(620, 290)
ray(ax, [Q(400, 1433), top], AXIAL, arrows=())
for y in (965, 1105):
    p = Q(400, 1433) + (top - Q(400, 1433)) * ((1433 - y) / (1433 - 290))
    head(ax, p, top - Q(400, 1433), AXIAL)
line(ax, Q(400, 1433), Q(400, 1803), **AXIAL)
line(ax, Q(603, 628), Q(1165, 632), **AXIAL)
line(ax, Q(545, 680), Q(1108, 545), **AXIAL)
for foot, tip in ((Q(400, 1800), Q(340, 1455)), (Q(603, 1785), Q(545, 1455))):
    line(ax, foot, tip, **AXIAL)
    head(ax, tip, tip - foot, AXIAL, 1.3)
    th0, th1 = 90, 90 + np.degrees(np.arctan2(foot[0] - tip[0], tip[1] - foot[1]))
    arc(ax, foot, 2.7, th0, th1, s=r"$\theta$", rt=1.12, size=8)
for p in (C, A, B, Q(752, 630), Q(1108, 545), Q(1108, 632)):
    dot(ax, p, ms=2.6)
# coordinate frame: X axis to the left from O, Z up, P at theta from Z, S2's extension meeting O at alpha
ax.annotate("", Q(120, 1705), O, arrowprops=dict(arrowstyle=ARROW, color=INK, lw=0.5, shrinkA=0, shrinkB=0))
ax.annotate("", Q(1487, 1270), O, arrowprops=dict(arrowstyle=ARROW, color=INK, lw=0.5, shrinkA=0, shrinkB=0))
ax.annotate("", Q(1435, 1405), O, arrowprops=dict(arrowstyle=ARROW, color=INK, lw=0.5, shrinkA=0, shrinkB=0, linestyle=(0, (4, 2))))
dash(ax, Q(855, 1762), O)
ang_s2 = np.degrees(np.arctan2(O[1] - Q(855, 1762)[1], O[0] - Q(855, 1762)[0]))
arc(ax, O, 2.6, 180 + ang_s2, 180, s=r"$\alpha$", rt=1.08, size=8, both=True)
ang_p = np.degrees(np.arctan2(*(Q(1435, 1405) - O)[::-1]))
arc(ax, O, 2.2, 90, ang_p, s=r"$\theta$", rt=1.3, size=8, both=True)
# labels as printed (sentence case, as in the other ch16 schematics)
text(ax, "$H$, illuminated pinhole", Q(640, 335), ha="left", size=7.5)
text(ax, "beam splitter", Q(475, 727), ha="right", size=7.5)
text(ax, "$H_1$", Q(758, 685))
text(ax, "$L_2$, eye lens or\ncamera", Q(870, 845), size=7.5, linespacing=1.1)
text(ax, "retina or\nimage plane", Q(1240, 785), size=7.5, linespacing=1.1)
text(ax, "$C'$", Q(1145, 550))
text(ax, "$A'$", Q(1145, 668))
text(ax, "$L_1$, collimating lens", Q(395, 1388), ha="right", size=7.5)
text(ax, "$R$", Q(512, 1457))
text(ax, "$C$", Q(420, 1683))
text(ax, "$S_1$", Q(490, 1730))
text(ax, "$A$", Q(633, 1685))
text(ax, "$d$", Q(622, 1740))
text(ax, "$S_2$", Q(498, 1795))
text(ax, "$B$", Q(605, 1825))
text(ax, "$X$", Q(88, 1705))
text(ax, "$Z$", Q(1490, 1243))
text(ax, "$P$", Q(1417, 1380))
text(ax, "$O$", Q(1505, 1708), ha="left")
done(fig, HERE)
readme(HERE, "Fig 16.2: notation with respect to the Fizeau interferoscope or interferometer", lines=[
    "Construction schematic, laid out at the scan's own geometry (docs/scans/ch16.pdf page 4): ideal thin lenses L1 (collimating)",
    "and L2 (eye lens or camera), the illuminated pinhole H at L1's focus, a beam splitter (a single line, as printed) imaging H at H1,",
    "the optical flat with lower face S1 on the X axis, and the inclined surface S2 below it. Points C, A, B, C', A', distance d, angle",
    "theta of the reflected ray R, wedge angle alpha (exaggerated, as on the scan) and the X, Z, P frame at O are the scan's own symbols.",
    "No numbers are printed on the figure and none are added.",
    "Spec correction: gap_pages_figure_specs.md describes 16.2 as a sine wave of phase delta against distance z (a caption from",
    "elsewhere); the scan's Figure 16.2 is this Fizeau notation diagram, and the manifest had bucketed it as a Matplotlib plot."])
