# Profile visual assets

The introduction is a locally rendered GIF, with separate light/dark assets and static PNG fallbacks. No hosted typing widget, JavaScript or remote fonts are used. Text expresses interests and project direction, not employment titles or professional certifications.

Regenerate from the repository root:

```sh
python -m pip install Pillow
python tools/generate_typewriter.py
```

The generator uses DejaVu Sans / DejaVu Sans Mono. Install DejaVu fonts, or set `FONT_DIR` to their directory. The animation plays once and settles; static images are linked in the README and selected for reduced motion where supported.

## Technology icons

The committed tiles contain SVG paths from [Simple Icons](https://github.com/simple-icons/simple-icons), with local framing and contrast-adjusted colors. The brand names identify tools, not endorsements or proficiency ratings. Upstream assets were retrieved on 24 October 2026; see the upstream repository for licensing and trademark guidance.

- Python: https://github.com/simple-icons/simple-icons/blob/develop/icons/python.svg
- PyTorch: https://github.com/simple-icons/simple-icons/blob/develop/icons/pytorch.svg
- NumPy: https://github.com/simple-icons/simple-icons/blob/develop/icons/numpy.svg
- ONNX: https://github.com/simple-icons/simple-icons/blob/develop/icons/onnx.svg
- FastAPI: https://github.com/simple-icons/simple-icons/blob/develop/icons/fastapi.svg
- Streamlit: https://github.com/simple-icons/simple-icons/blob/develop/icons/streamlit.svg
- JavaScript: https://github.com/simple-icons/simple-icons/blob/develop/icons/javascript.svg
- React: https://github.com/simple-icons/simple-icons/blob/develop/icons/react.svg
- Next.js: https://github.com/simple-icons/simple-icons/blob/develop/icons/nextdotjs.svg
- PostgreSQL: https://github.com/simple-icons/simple-icons/blob/develop/icons/postgresql.svg
- Git: https://github.com/simple-icons/simple-icons/blob/develop/icons/git.svg

The README table ties technologies to inspected project evidence. Technologies shown in the supplied reference but unsupported by the inspected work were not copied.
