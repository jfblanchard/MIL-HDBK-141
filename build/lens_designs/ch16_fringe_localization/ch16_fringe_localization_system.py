"""Fig 16.13: why Fizeau fringes appear localized at P near the reflecting surfaces.
A point source S sends two rays to a thin air wedge (S1 upper surface, S2 lower, wedge
angle theta, medium n1). Ray 1 reflects off S1 at D; ray 2 enters the gap and reflects
off S2 at Q. The reflected rays cross at P beside the surfaces, and the eye lens images
that neighbourhood onto the retina at P'. Dashed continuations locate the virtual
source images s1, s2 behind the wedge."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

fig, ax = canvas(TEXT_WIDTH * 0.62, (-18, 72), (-80, 68))

# --- wedge surfaces -------------------------------------------------------
s1a, s1b = P(-8, 0.0), P(70, 0.0)                 # S1 horizontal
ang = -4.5                                          # wedge angle, exaggerated
s2a = P(-8, -1.6)
s2b = s2a + np.array([78, 78 * np.tan(np.radians(ang))])
line(ax, s1a, s1b, color=INK, linewidth=1.2, solid_capstyle="butt", zorder=3)
line(ax, s2a, s2b, color=INK, linewidth=1.2, solid_capstyle="butt", zorder=3)
text(ax, "$S_1$", P(-12, 0.4), ha="right", size=8)
text(ax, "$S_2$", P(-12, -2.4), ha="right", size=8)
text(ax, "$n_1$", P(54, -3.0), size=8)
arc(ax, P(64, -1.9), 4.5, -2.5, 2.0, "$\\theta$", rt=1.9, size=7)

# --- source and incident rays ---------------------------------------------
S = P(-4, 58)
dot(ax, S, ms=2)
text(ax, "S, POINT IN SOURCE", P(-4, 62), size=7)

D = P(26, 0.0)                                    # reflection point on S1
Q = P(28.6, -4.35)                                # reflection point on S2
Pnt = P(28.5, 1.3)                                # localisation point beside the surfaces
r1 = unit(Pnt - D)                                 # reflected ray off S1
r2 = unit(Pnt - Q)                                 # reflected ray off S2
ray(ax, [S, D], AXIAL, arrows=(0.55,))
ray(ax, [S, Q], AXIAL, arrows=(0.55,))
ray(ax, [D, Pnt], AXIAL)
ray(ax, [Q, Pnt], AXIAL)
dot(ax, D, ms=2); dot(ax, Q, ms=2); dot(ax, Pnt, ms=2)

# --- reflected rays to the eye ---------------------------------------------
eye_dir = unit(r1 + r2)
lens_c = Pnt + eye_dir * 30
# eye lens perpendicular to the mean ray
tl = rot(eye_dir, 90)
tlens(ax, lens_c - eye_dir * 3.5, 5.5, np.degrees(np.arctan2(tl[1], tl[0])))
Pp = lens_c + eye_dir * 10                          # P' on the retina
line(ax, Pp + rot(eye_dir, 90) * 7, Pp - rot(eye_dir, 90) * 7, color=INK, linewidth=1.0)
dot(ax, Pp, ms=2)
ray(ax, [Pnt, lens_c - eye_dir * 3.5], AXIAL, arrows=(0.6,))
ray(ax, [lens_c - eye_dir * 3.5, Pp], AXIAL, arrows=(0.6,))
ray(ax, [Pnt + 1.6 * r2, lens_c - eye_dir * 3.5 + 1.6 * tl], AXIAL, arrows=(0.6,))
ray(ax, [lens_c - eye_dir * 3.5 + 1.6 * tl, Pp], AXIAL, arrows=(0.6,))
text(ax, "EYE LENS", lens_c - eye_dir * 3.5 + tl * 8.5, size=7)
text(ax, "RETINA", Pp + rot(eye_dir, 90) * 8.5, size=7)
text(ax, "$P^\\prime$", Pp + rot(eye_dir, 90) * 1.6 + eye_dir * 1.5, size=8)

# --- virtual source images (dashed continuations) ---------------------------
s1p = P(-6, -52)
s2p = P(-9, -66)
dash(ax, D, s1p); dash(ax, Q, s2p)
dot(ax, s1p, ms=2); dot(ax, s2p, ms=2)
text(ax, "$s_1$", s1p + P(2.5, 0), ha="left", size=8)
text(ax, "$s_2$", s2p + P(2.5, 0), ha="left", size=8)

# --- labels ------------------------------------------------------------------
text(ax, "$D$", D + P(-1.5, 2.2), size=8)
text(ax, "$P$", Pnt + P(2.2, 2.0), size=8)
text(ax, "$Q$", Q + P(-2.0, -2.2), size=8)
lab(ax, "$d = QD$, APPROXIMATELY", (Q + D) / 2 + P(1, -1.2), P(52, -14), ha="left", size=7)
arc(ax, S + unit(D - S) * 14, 7, -95, -75, "$\\theta$", rt=1.8, size=7)
arc(ax, Pnt, 6, 80, 100, "$i$", rt=1.7, size=7)

done(fig, HERE)
readme(HERE, "Fig 16.13: Fizeau-fringe localisation construction",
       lines=["Pure geometric construction: wedge surfaces S1/S2, source S, reflections at D and Q,",
              "reflected rays crossing at P beside the wedge, imaged to P' on the retina.",
              "Dashed continuations mark the virtual source images s1, s2.",
              "Symbols as printed on the figure: theta (wedge/ray angle), i, n1, d = QD approximately."])
