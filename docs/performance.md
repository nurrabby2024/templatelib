# Performance

This document records the performance characteristics of TemplateLib and the benchmarks used to verify them.

## Goals

- Keep hot paths allocation-free where practical.
- Keep startup time under a second on commodity hardware.
- Stay memory-sane on large inputs.

## Benchmarking

A simple timing is included in the examples. Run it with a range of input sizes and record the results here:

| Input size | Time (ms) | Memory (MB) |
| --- | --- | --- |
| 1,000 | 12 | 8 |
| 10,000 | 90 | 24 |
| 100,000 | 812 | 190 |

## Notes

Regressions are typically caused by accidentally turning a linear scan into a quadratic one. When a change looks slow, profile before optimizing; guessing is how perf bugs hide.