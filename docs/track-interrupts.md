# Track Interrupts

###### Driver Support
| Code | Version |
| ---- | ------- |
| fscc-windows | 2.7.0 |
| pyfscc | 1.0.0 |


## Track Interrupts
```python
def track_interrupts(self, timeout=None):
```

| Parameter | Type  | Default | Description |
| --------- | ----- | ------- | ----------- |
| `timeout` | `int` | `None` | Number of milliseconds to wait for data before timing out |


###### Examples
```python
import fscc
...

# TIN interrupt
matches = p.track_interrupts(0x00000400)
```


### Additional Resources
- Complete example: [`examples/track-interrupts.py`](../examples/track-interrupts.py)
- Implementation details: [`fscc.py`](../fscc/port.py)
