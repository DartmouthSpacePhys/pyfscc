# Connect

Opening a handle using this API will only give you access to the
synchronous functionality of the card. You will need to use the COM ports
if you would like to use the asynchronous functionality.

###### Driver Support
| Code           | Version
| -------------- | --------
| `fscc-windows` | `v2.0.0`
| `fscc-linux`   | `v2.0.0`
| `pyfscc`       | `v1.0.0`


## Connect
```python
def __init__(self, port_num, append_status=True, append_timestamp=True)
```

###### Examples
```python
import fscc
...

p = Port(0)
```


### Additional Resources
- Complete example: [`examples\tutorial.py`](https://github.com/commtech/netfscc/blob/master/examples/tutorial.py)
- Implemenation details: [`src\fscc.py`](https://github.com/commtech/netfscc/blob/master/src/fscc.py)