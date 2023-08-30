from pylint.lint import Run

# results = Run(['test_base.py'], do_exit=False)
# `exit` is deprecated, use `do_exit` instead
# print(results.linter.stats['global_note'])


score = Run(['test_base.py'], exit=False).linter.stats.global_note
print(score)
