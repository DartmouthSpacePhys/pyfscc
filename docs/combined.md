# Connect

Opening a handle using this API will only give you access to the synchronous functionality of the card. You will need to use the COM ports if you would like to use the asynchronous functionality.

###### Driver Support
| Code | Version |
| ---- | ------- |
| fscc-windows | 2.0.0 |
| fscc-linux | 2.0.0 |
| pyfscc | 1.0.0 |


## Connect
```python
def __init__(self, port_num, append_status=True, append_timestamp=True)
```

| Exception | Base Exception | Cause |
| --------- | -------------- |------ |
| `PortNotFoundError` | `OSError` | Port not found |
| `InvalidAccessError` | `OSError` | Insufficient permissions |

###### Examples
```python
import fscc
...

p = fscc.Port(0)
```


### Additional Resources
- Complete example: [`examples/tutorial.py`](../examples/tutorial.py)
- Implementation details: [`fscc.py`](../fscc/port.py)
# Registers

The FSCC driver is a Swiss army knife of sorts with communication. It can handle many different situations, if configured correctly. Typically to configure it to handle your specific situation you need to modify the card's register values.

_For a complete listing of all of the configuration options please see the manual._

In HDLC mode some settings are fixed at certain values. If you are in HDLC mode and after setting/getting your registers some bits don't look correct, then they are likely fixed. A complete list of the fixed values can be found in the `CCR0` section of the manual.

_The read-only registers will return the value of the `VSTR` register upon reading._

All of the registers, except `FCR`, are tied to a single port. `FCR` on the other hand is shared between two ports on a card. You can differentiate between which `FCR` settings affects what port by the A/B labels. A for port 0 and B for port 1.

_A [`purge()`](https://github.com/commtech/pyfscc/blob/master/docs/purge.md) (receive side) is required after changing the `MODE` bits in the `CCR0` register. If you need to change the `MODE` bits but don't have a clock present, change the `CM` bits to `0x7` temporarily. This will give you an internal clock to switch modes. You can then switch to your desired `CM` now that your `MODE` is locked in._

###### Driver Support
| Code | Version |
| ---- | ------- |
| fscc-windows | 2.0.0 |
| fscc-linux | 2.0.0 |
| pyfscc | 1.0.0 |


## Property
```python
registers = property(...)
```


## Set
###### Examples
```python
import fscc
...

p.registers.CCR0 = 0x0011201c
p.registers.BGR = 0
```


## Get
###### Examples
```python
import fscc
...

ccr1 = p.registers.CCR1
ccr2 = p.registers.CCR2
```


### Additional Resources
- Complete example: [`examples/registers.py`](../examples/registers.py)
- Implementation details: [`fscc.py`](../fscc/port.py)
# Clock Frequency

The FSCC device has a programmable clock that can be set anywhere from 20 KHz to 200 MHz. However, this is not the full operational range of an FSCC port, only the range that the on-board clock can be set to.

Using one of the synchronous modes you can only receive data consistently up to 30 MHz (when you are using an external clock). If you are transmitting data using an internal clock, you can safely receive data consistently up to 50 MHz.

Lower clock rates (less than 1 MHz for example) can take a long time for the frequency generator to finish. If you run into this situation we recommend using a larger frequency and then dividing it down to your desired baud rate using the `BGR` register.

_If you are receiving timeout errors when using slow data rates you can bypass the safety checks by using the [`ignore_timeout`](https://github.com/commtech/pyfscc/blob/master/docs/ignore-timeout.md) option._

###### Driver Support
| Code | Version |
| ---- | ------- |
| fscc-windows | 2.0.0 |
| fscc-linux | 2.0.0 |
| pyfscc | 1.0.0 |

## Property
```python
clock_frequency = property(...)
```

## Set

| Exception | Base Exception | Cause |
| --------- | -------------- | ----- |
| `InvalidParameterError` | `ValueError` | Clock frequency is out of range (15,000 to 270,000,000) |

###### Examples
```python
import fscc
...

# 18.432 MHz
p.clock_frequency = 18432000
```


### Additional Resources
- Complete example: [`examples/clock-frequency.py`](../examples/clock-frequency.py)
- Implementation details: [`fscc.py`](../fscc/port.py)
# Append Status

It is a good idea to pay attention to the status of each frame. For example, you may want to see if the frame's CRC check succeeded or failed.

The FSCC reports this data to you by appending two additional bytes to each frame you read from the card, if you opt-in to see this data. There are a few methods of enabling this additional data.

###### Support
| Code | Version |
| ---- | ------- |
| fscc-windows | 2.0.0 |
| fscc-linux | 2.0.0 |
| pyfscc | 1.0.0 |


## Property
```python
append_status = property(...)
```


## Get
###### Examples
```python
import fscc
...

status = p.append_status
```


## Enable
###### Examples
```python
import fscc
...

p.append_status = True
```


## Disable
###### Examples
```python
import fscc
...

p.append_status = False
```


### Additional Resources
- Complete example: [`examples/append-status.py`](../examples/append-status.py)
- Implementation details: [`fscc.py`](../fscc/port.py)
# Append Timestamp

###### Windows
[`KeQuerySystemTime`](http://msdn.microsoft.com/en-us/library/windows/hardware/ff553068.aspx) is used to acquire the timestamp upon complete reception of a frame.

###### Linux
[`do_gettimeofday`](http://www.fsl.cs.sunysb.edu/kernel-api/re29.html) is used to acquire the timestamp upon complete reception of a frame.

_We will be moving to [`getnstimeofday`](http://www.gnugeneration.com/books/linux/2.6.20/kernel-api/re32.html) in the 3.0 driver series._


###### Support
| Code | Version |
| ---- | ------- |
| fscc-windows | 2.4.0 |
| fscc-linux | 2.4.0 |
| pyfscc | 2.0.0 |


## Property
```python
append_timestamp = property(...)
```


## Get
###### Examples
```python
import fscc
...

status = p.append_timestamp
```


## Enable
###### Examples
```python
import fscc
...

p.append_timestamp = True
```


## Disable
###### Examples
```python
import fscc
...

p.append_timestamp = False
```


### Additional Resources
- Complete example: [`examples/append-timestamp.py`](../examples/append-timestamp.py)
- Implementation details: [`fscc.py`](../fscc/port.py)
# Ignore Timeout

###### Support
| Code | Version |
| ---- | ------- |
| fscc-windows | 2.0.0 |
| fscc-linux | 2.0.0 |
| pyfscc | 1.0.0 |


## Property
```python
ignore_timeout = property(...)
```


## Get
###### Examples
```python
import fscc
...

status = p.ignore_timeout
```


## Enable
###### Examples
```python
import fscc
...

p.ignore_timeout = True
```


## Disable
###### Examples
```python
import fscc
...

p.ignore_timeout = False
```


### Additional Resources
- Complete example: [`examples/ignore-timeout.py`](../examples/ignore-timeout.py)
- Implementation details: [`fscc.py`](../fscc/port.py)
# Memory Cap

###### Support
| Code | Version |
| ---- | ------- |
| fscc-windows | 2.0.0 |
| fscc-linux | 2.0.0 |
| pyfscc | 1.0.0 |


## Property
```python
memory_cap = property(...)
```


## Get
###### Examples
```python
import fscc
...

input_cap = p.memory_cap.input
output_cap = p.memory_cap.output
```


## Set
###### Examples
```python
import fscc
...

p.memory_cap.input = 1000000  # 1MB
p.memory_cap.output = 1000000  # 1MB
```


### Additional Resources
- Complete example: [`examples/memory-cap.py`](../examples/memory-cap.py)
- Implementation details: [`fscc.py`](../fscc/port.py)
# Purge

Between the hardware FIFO and the driver's software buffers there are multiple places data could be stored, excluding your application code. If you ever need to clear this data and start fresh, there are a couple of methods you can use.

_A `purge()` (receive side)
is required after changing the `MODE` bits in the `CCR0` register. If you need to change the `MODE` bits but don't have a clock present, change the `CM` bits to `0x7` temporarily. This will give you an internal clock to switch modes. You can then switch to your desired `CM` now that your `MODE` is  locked in._

###### Driver Support
| Code | Version |
| ---- | ------- |
| fscc-windows | 2.0.0 |
| fscc-linux | 2.0.0 |
| pyfscc | 1.0.0 |


## Execute
```python
def purge(self, tx=True, rx=True)
```

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `tx` | `Boolean` | True | Whether to purge the transmit data |
| `rx` | `Boolean` | True | Whether to purge the receive data |

| Exception | Base Exception | Cause |
| --------- | -------------- | ----- |
| `TimeoutError` | `OSError` | Command timed out (missing clock) |

###### Examples
Purge both the transmit and receive data.
```python
using Fscc;
...

p.Purge(True, True)
```

Purge only the transmit data.
```python
using Fscc;
...

p.Purge(True, False)
```

Purge only the receive data.
```python
using Fscc;
...

p.Purge(False, True)
```


### Additional Resources
- Complete example: [`examples/purge.py`](../examples/purge.py)
- Implementation details: [`fscc.py`](../fscc/port.py)
# Read

The `size` argument of the various read functions means different things depending on the mode you are using.

In a frame based mode the `size` argument specifies the maximum frame `size` to return. If the next queued frame is larger than the size you specified the error `FSCC_BUFFER_TOO_SMALL` is returned and the data will remain waiting for a read of a larger value. If a `size` is specified that is larger than the length of multiple frames in queue, you will still only receive one frame per read call.

In streaming mode (no frame termination) the `size` argument specifies the maximum amount of data to return. If there are 100 bytes of streaming data in the card and you read with a `size` of 50, you will receive 50 bytes. If you do a read of 200 bytes, you will receive the 100 bytes available.

Frame based data and streaming data are kept separate within the driver. To understand what this means, first imagine the following scenario. You are in a frame based mode and receive a couple of frames. You then switch to streaming mode and receive a stream of data. When calling read you will receive the the streaming data until you switch back into a frame based mode and do a read.

###### Driver Support
| Code | Version |
| ---- | ------- |
| fscc-windows | 2.0.0 |
| fscc-linux | 2.0.0 |
| pyfscc | 1.0.0 |


## Read
```python
def read(self, timeout=None, size=4096):
```

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `timeout` | `int` | `None` | Number of milliseconds to wait for data before timing out |
| `size` | `int` | 4096 | The data buffer size |

| Exception | Base Exception | Cause |
| --------- | -------------- | ----- |
| `BufferTooSmallError` | `OSError` | The buffer size is smaller than the next frame |
| `IncorrectModeError` | `OSError` | Using the synchronous port while in asynchronous mode |

###### Examples
```python
import fscc
...

p.read(100)
```


### Additional Resources
- Complete example: [`examples/tutorial.py`](../examples/tutorial.py)
- Implementation details: [`fscc.py`](../fscc/port.py)
# Write

###### Driver Support
| Code | Version |
| ---- | ------- |
| fscc-windows | 2.0.0 |
| fscc-linux | 2.0.0 |
| pyfscc | 1.0.0 |


## Write
```python
def write(self, data):
```

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `buf` | `bytes` | The data buffer to transmit |

| Return
| ---------------------------
| Number of bytes transmitted

| Exception | Base Exception | Cause |
| --------- | -------------- | ----- |
| `BufferTooSmallError` | `OSError` | The write size exceeds the output memory usage cap |
| `TimeoutError` | `OSError` | Command timed out (missing clock) |
| `IncorrectModeError` | `OSError` | Using the synchronous port while in asynchronous mode |

###### Examples
```python
import fscc
...

p.write(b'Hello world!')
```


### Additional Resources
- Complete example: [`examples/tutorial.py`](../examples/tutorial.py)
- Implementation details: [`fscc.py`](../fscc/port.py)
# RX Multiple

###### Support
| Code | Version |
| ---- | ------- |
| fscc-windows | 2.0.0 |
| fscc-linux | 2.0.0 |
| pyfscc | 1.0.0 |


## Property
```python
rx_multiple = property(...)
```


## Get
###### Examples
```python
import fscc
...

status = p.rx_multiple
```


## Enable
###### Examples
```python
import fscc
...

p.rx_multiple = True
```


## Disable
###### Examples
```python
import fscc
...

p.rx_multiple = False
```


### Additional Resources
- Complete example: [`examples/rx-multiple.py`](../examples/rx-multiple.py)
- Implementation details: [`fscc.py`](../fscc/port.py)
# TX Modifiers

| Modifiers | Value | Description |
| --------- | -----:| ----------- |
| `XF` | 0 | Normal transmit (disable modifiers) |
| `XREP` | 1 | Transmit frame repeatedly |
| `TXT` | 2 | Transmit frame on timer |
| `TXEXT` | 4 | Transmit frame on external signal |

###### Support
| Code | Version |
| ---- | ------- |
| fscc-windows | 2.0.0 |
| fscc-linux | 2.0.0 |
| pyfscc | 1.0.0 |


## Property
```python
tx_modifiers = property(...)
```


## Get
###### Examples
```python
import fscc
...

modifiers = p.tx_modifiers
```


## Set
###### Examples
```python
import fscc
...

p.tx_modifiers = TXT | XREP
```


### Additional Resources
- Complete example: [`examples/tx-modifiers.py`](../examples/tx-modifiers.py)
- Implementation details: [`fscc.py`](../fscc/port.py)
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
