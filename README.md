
Project Report: The Impact of Alcohol on Coding Skills

This repository contains the code, data, and small analysis used for the student project "The Impact of Alcohol on Coding Skills" by Taras Zinchenko and Nikita Marfitsyn (April 2025). The code is written in Python and shows how alcohol affects simple coding tasks in a small experiment of 10 participants.

What this project does (short story)
- We collected simple coding task results and short surveys from 10 volunteers. Each person solved similar problems at different stages: sober, after 1 drink, after 2 drinks, and after 3 drinks.
- The code computes basic statistics (paired t-tests, Wilcoxon, correlations) and makes clear charts that show average time, lines of code, confidence, and concentration.
- The goal is to explore how even small amounts of alcohol change coding speed, efficiency, and self-confidence.

Key findings (simple language)
- Any drinking usually makes coding worse. Most people wrote more lines and took more time after they drank.
- A small, short improvement after the first drink was seen in this data (sometimes called the "Ballmer Peak" idea), but the effect is not reliable.
- Performance drops more after two drinks. After three drinks some people could not finish tasks, so averages may look lower but that is because they stopped early.
- More experienced coders showed a smaller drop in performance, but everyone was affected to some degree.

Limitations (be careful)
- This study used only 10 people. That is a small sample and limits what we can claim.
- Tasks had small differences in topic, and some participants could not finish some tasks. These facts can change results.

Quick start — run the analysis and create outputs
1. Create and activate a virtual environment, then install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

2. Generate plots (saved to `outputs/`):

```powershell
project-report-plots --out outputs
# or
python scripts\run_plots.py --out outputs
```

3. Run statistical tests and save results:

```powershell
project-report-stats --out outputs\stats.json
# or
python scripts\run_stats.py --out outputs\stats.json
```

4. Run the (small) tests:

```powershell
pip install pytest
pytest -q
```

Project layout (short)
- `src/project_report/` — main package with `data.py`, `analysis.py`, `plotting.py`, and `cli.py`.
- `scripts/` — thin CLI wrappers (also available as console scripts after `pip install -e .`).
- `examples/legacy_scripts/` — original scripts kept for reference.
- `outputs/` — generated charts and `stats.json` (not tracked by git).
- `requirements.txt` and `requirements-pinned.txt` — dependency lists.

Context and report
The full written report and more context live in the project files and the PDF report. The main report describes the experiment, results, and citations in more detail. You can find the original data and links referenced in Appendix A of the report.

If you want me to help further
- I can rewrite parts of the code to use CSV input, add clearer unit tests for `analysis.py`, or prepare a short presentation slide with the key charts.
- I can also make the README shorter or longer, or change the language level if you prefer more technical wording.

Credits & Links
- Authors: Taras Zinchenko, Nikita Marfitsyn (April 2025)
- Original analysis code repository: https://github.com/TarasZinchenko/ProjectReportCode.git
- Data (Google Sheets): see Appendix A in the report.

License
This repository does not set a formal license. Tell me if you want an open license (for example MIT) added.

The Impact of Alcohol on Coding Skills
This project investigates the effects of alcohol consumption on essential coding skills: speed, productivity, and error rates.

Main Research Question:

What is the impact of alcohol consumption on coding speed, productivity, and the number of errors made while programming?

Methodology:

The study employed a mixed-methods approach combining:

Experiments: Participants completed coding tasks before and after consuming varying amounts of alcohol, measuring speed, lines of code, and errors.

Surveys: Data on participants' characteristics, drinking habits, and subjective perceptions were collected.

Key Findings:

The study found that alcohol consumption negatively impacts coding performance. Coding speed generally decreased, efficiency declined (more lines of code written), and error rates increased with higher alcohol consumption. More experienced coders showed slightly better resilience but still experienced performance declines.

Data and Analysis Code:

Data: https://docs.google.com/spreadsheets/d/1b5EF8hMXZeiRcnd58qt2aN0FUA6JxMrjqUb8-ov5hhk/edit?resourcekey=&gid=1603492440#gid=1603492440
