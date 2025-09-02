try:
    from typing import TYPE_CHECKING as __TYPE_CHECKING
except:
    __TYPE_CHECKING = False

if __TYPE_CHECKING:
    from typing import Any, Optional, Union, List, Tuple
    
    class iovec:
        """Vector I/O data structure"""
        ref: List[Any]
        ptr: Any
        len: int
        
        def __init__(self, buffers: Union[bytes, bytearray, memoryview, List[Any], Tuple[Any, ...]]) -> None: ...
        def __bool__(self) -> bool: ...
        def __len__(self) -> int: ...
        def __getitem__(self, index: int) -> "iovec": ...
        
        @property
        def iov_base(self) -> Any: ...
        
        @property
        def iov_len(self) -> int: ...
    
    class open_how:
        """How to Open a Path"""
        ptr: Any
        
        def __init__(self, flags: int = 0, mode: int = 0, resolve: int = 0) -> None: ...
        def __repr__(self) -> str: ...
        
        @property
        def mode(self) -> int: ...
        
        @mode.setter
        def mode(self, mode: int) -> None: ...
        
        @property
        def flags(self) -> int: ...
        
        @flags.setter
        def flags(self, flags: int) -> None: ...
        
        @property
        def resolve(self) -> int: ...
        
        @resolve.setter
        def resolve(self, resolve: int) -> None: ...
    
    class futex_state:
        """Futex State - User Address Memory"""
        ptr: Any
        len: int
        private: bool
        
        def __init__(self, num: int = 1, private: bool = False) -> None: ...
        def __repr__(self) -> str: ...
        
        @property
        def state(self) -> int: ...
        
        @state.setter
        def state(self, value: int) -> None: ...
    
    class futex_waitv:
        """A Waiter For Vectorized Wait"""
        ptr: Any
        private: bool
        len: int
        
        def __init__(self, futex: futex_state) -> None: ...
        
        @property
        def val(self) -> int: ...
        
        @val.setter
        def val(self, val: int) -> None: ...
        
        @property
        def flags(self) -> int: ...
        
        @flags.setter
        def flags(self, flags: int) -> None: ...
    
    class sockaddr:
        """Generic Socket Address"""
        ptr: Any
        free: bool
        sizeof: int
        family: int
        
        def __init__(
            self, 
            family: int = 0, 
            addr: bytes = b'', 
            port: int = 0, 
            scope_id: int = 0
        ) -> None: ...
        def __repr__(self) -> str: ...
    
    class msghdr:
        """Message header for socket operations"""
        ptr: Any
        
        def __init__(self) -> None: ...
    
    class cmsghdr:
        """Control message header"""
        ptr: Any
        
        def __init__(self) -> None: ...
    
    class io_uring_recvmsg_out:
        """Recvmsg output structure"""
        ptr: Any
        
        def __init__(self) -> None: ...
    
    class epoll_event:
        """Epoll event structure"""
        ptr: Any
        
        def __init__(self) -> None: ...
    
    class io_uring_probe:
        """IO uring probe structure"""
        ptr: Any
        len: int
        
        def __init__(self, num: int = 0) -> None: ...
        
        @property
        def last_op(self) -> int: ...
        
        @property
        def ops_len(self) -> int: ...
    
    class statx:
        """Extended file attribute retrieval structure"""
        ptr: Any
        
        def __init__(self) -> None: ...
        
        @property
        def stx_mask(self) -> int: ...
        
        @property
        def stx_blksize(self) -> int: ...
        
        @property
        def stx_attributes(self) -> int: ...
        
        @property
        def stx_nlink(self) -> int: ...
        
        @property
        def stx_uid(self) -> int: ...
    
    class timespec:
        """Kernel Timespec"""
        ptr: Any
        
        def __init__(self, second: float = 0) -> None: ...
        
        @property
        def tv_sec(self) -> int: ...
        
        @tv_sec.setter
        def tv_sec(self, second: int) -> None: ...
        
        @property
        def tv_nsec(self) -> int: ...
        
        @tv_nsec.setter
        def tv_nsec(self, nanosecond: int) -> None: ...
    
    class io_uring:
        """I/O URing"""
        flags: int
        ring_fd: int
        features: int
        enter_ring_fd: int
        int_flags: int
        active: bool
        
        def __repr__(self) -> str: ...

    class io_uring_sqe:
        """IO submission data structure (Submission Queue Entry)"""
        flags: int
        user_data: int
        
        def __init__(self, num: int = 1, *args: Any, **kwargs: Any) -> None: ...
        def __bool__(self) -> bool: ...
        def __len__(self) -> int: ...
        def __getitem__(self, index: int) -> "io_uring_sqe": ...

    class io_uring_cqe:
        """IO completion data structure (Completion Queue Entry)"""
        user_data: int
        res: int
        flags: int
        
        def __getitem__(self, index: int) -> "io_uring_cqe": ...
        def __bool__(self) -> bool: ...
        def __repr__(self) -> str: ...
        def get_index(self, index: int) -> tuple[int, int]: ...

    class io_uring_params:
        """io_uring parameters"""
        pass

    class io_uring_buf_ring:
        """io_uring buffer ring"""
        pass

    class io_uring_reg_wait:
        """io_uring registered wait structure"""
        pass

    class timespec:
        """Timespec structure"""
        pass

    class siginfo:
        """Signal info structure"""
        pass

    class sigset:
        """Signal set structure"""
        pass

    # Queue initialization and management functions
    def io_uring_queue_init_mem(
        entries: int, 
        ring: io_uring, 
        p: io_uring_params, 
        buf: memoryview, 
        buf_size: int
    ) -> int: 
        """Initialize io_uring queue with pre-allocated memory.
        
        Docs: https://man7.org/linux/man-pages/man3/io_uring_queue_init_mem.3.html

        Args:
            entries: Number of queue entries to initialize
            ring: io_uring structure to initialize
            p: Parameters for initialization
            buf: Pre-allocated memory buffer
            buf_size: Size of the buffer
            
        Returns:
            0 on success, negative error code on failure
        """
        ...
    
    def io_uring_queue_init_params(entries: int, ring: io_uring, p: io_uring_params) -> int: 
        """Initialize io_uring queue with parameters.
        
        Docs: https://man7.org/linux/man-pages/man3/io_uring_queue_init_params.3.html

        Args:
            entries: Number of queue entries to initialize
            ring: io_uring structure to initialize
            p: Parameters for initialization
            
        Returns:
            0 on success, negative error code on failure
        """
        ...
    
    def io_uring_queue_init(entries: int, ring: io_uring, flags: int = 0) -> int: 
        """Initialize io_uring queue with default parameters.

        Docs: https://man7.org/linux/man-pages/man3/io_uring_queue_init.3.html

        Args:
            entries: Number of queue entries to initialize
            ring: io_uring structure to initialize
            flags: Optional flags for initialization
            
        Returns:
            0 on success, negative error code on failure
        """
        ...

    def io_uring_queue_mmap(fd: int, p: io_uring_params, ring: io_uring) -> int: 
        """Memory map io_uring queues from file descriptor.
        
        Docs: [lord of io_uring](https://unixism.net/loti/ref-liburing/setup_teardown.html#:~:text=int-,io_uring_queue_mmap,-(int%20fd)

        Args:
            fd: File descriptor of io_uring instance
            p: Parameters structure
            ring: io_uring structure to initialize
            
        Returns:
            0 on success, negative error code on failure
        """
        ...
    
    io_uring_queue_mmap

    def io_uring_ring_dontfork(ring: io_uring) -> int: 
        """Mark io_uring ring as not inheritable by child processes.
        
        Docs: [Lord of io_uring](https://unixism.net/loti/ref-liburing/setup_teardown.html#:~:text=io_uring_ring_dontfork)

        Args:
            ring: io_uring structure
            
        Returns:
            0 on success, negative error code on failure
        """
        ...
    
    def io_uring_queue_exit(ring: io_uring) -> int: 
        """Clean up and exit io_uring queue.
        
        Docs: https://man7.org/linux/man-pages/man3/io_uring_queue_exit.3.html

        Args:
            ring: io_uring structure to clean up
            
        Returns:
            0 on success, negative error code on failure
        """
        ...

    # CQE handling functions
    def io_uring_peek_batch_cqe(ring: io_uring, cqes: io_uring_cqe, count: int) -> int: 
        """Peek at multiple completion queue entries without consuming them.
        
        Docs: https://man7.org/linux/man-pages/man3/io_uring_peek_batch_cqe.3.html

        Args:
            ring: io_uring structure
            cqes: Array to store completion queue entries
            count: Maximum number of entries to peek
            
        Returns:
            Number of entries peeked, or negative error code
        """
        ...
    
    def io_uring_wait_cqes(
        ring: io_uring, 
        cqe_ptr: io_uring_cqe, 
        wait_nr: int, 
        ts: Optional[timespec] = None, 
        sigmask: Optional[sigset] = None
    ) -> int: 
        """Wait for completion queue entries.
        
        Docs: https://man7.org/linux/man-pages/man3/io_uring_wait_cqes.3.html

        Args:
            ring: io_uring structure
            cqe_ptr: Pointer to store completion queue entry
            wait_nr: Number of entries to wait for
            ts: Optional timeout
            sigmask: Optional signal mask
            
        Returns:
            0 on success, negative error code on failure
        """
        ...
    
    def io_uring_wait_cqes_min_timeout(
        ring: io_uring,
        cqe_ptr: io_uring_cqe,
        wait_nr: int,
        ts: timespec,
        min_ts_usec: int,
        sigmask: Optional[sigset] = None
    ) -> int: 
        """Wait for completion queue entries with minimum timeout.
        
        Docs: https://man7.org/linux/man-pages/man3/io_uring_wait_cqes_min_timeout.3.html

        Args:
            ring: io_uring structure
            cqe_ptr: Pointer to store completion queue entry
            wait_nr: Number of entries to wait for
            ts: Timeout specification
            min_ts_usec: Minimum timeout in microseconds
            sigmask: Optional signal mask
            
        Returns:
            0 on success, negative error code on failure
        """
        ...
    
    def io_uring_wait_cqe_timeout(ring: io_uring, cqe_ptr: io_uring_cqe, ts: timespec) -> int: 
        """Wait for a single completion queue entry with timeout.
        
        Docs: https://man7.org/linux/man-pages/man3/io_uring_wait_cqe_timeout.3.html

        Args:
            ring: io_uring structure
            cqe_ptr: Pointer to store completion queue entry
            ts: Timeout specification
            
        Returns:
            0 on success, negative error code on failure
        """
        ...

    # Submission functions
    def io_uring_submit(ring: io_uring) -> int: 
        """Submit all prepared submission queue entries.
        
        Docs: https://man7.org/linux/man-pages/man3/io_uring_submit.3.html

        Args:
            ring: io_uring structure
            
        Returns:
            Number of submitted entries, or negative error code
        """
        ...
    
    def io_uring_submit_and_wait(ring: io_uring, wait_nr: int) -> int: 
        """Submit entries and wait for completions.
        
        Docs: https://man7.org/linux/man-pages/man3/io_uring_submit_and_wait.3.html

        Args:
            ring: io_uring structure
            wait_nr: Number of completions to wait for
            
        Returns:
            Number of submitted entries, or negative error code
        """
        ...
    
    def io_uring_submit_and_wait_timeout(
        ring: io_uring,
        cqe_ptr: io_uring_cqe,
        wait_nr: int,
        ts: Optional[timespec] = None,
        sigmask: Optional[sigset] = None
    ) -> int: 
        """Submit entries and wait for completions with timeout.
        
        Docs: https://man7.org/linux/man-pages/man3/io_uring_submit_and_wait_timeout.3.html

        Args:
            ring: io_uring structure
            cqe_ptr: Pointer to store completion queue entry
            wait_nr: Number of completions to wait for
            ts: Optional timeout
            sigmask: Optional signal mask
            
        Returns:
            Number of submitted entries, or negative error code
        """
        ...
    
    def io_uring_submit_and_wait_min_timeout(
        ring: io_uring,
        cqe_ptr: io_uring_cqe,
        wait_nr: int,
        ts: timespec,
        min_wait: int,
        sigmask: Optional[sigset] = None
    ) -> int: 
        """Submit entries and wait for completions with minimum timeout.
        
        Docs: https://man7.org/linux/man-pages/man3/io_uring_submit_and_wait_min_timeout.3.html

        Args:
            ring: io_uring structure
            cqe_ptr: Pointer to store completion queue entry
            wait_nr: Number of completions to wait for
            ts: Timeout specification
            min_wait: Minimum wait time
            sigmask: Optional signal mask
            
        Returns:
            Number of submitted entries, or negative error code
        """
        ...
    
    def io_uring_submit_and_wait_reg(
        ring: io_uring, 
        cqe_ptr: io_uring_cqe, 
        wait_nr: int, 
        reg_index: int
    ) -> int: 
        """Submit entries and wait using registered wait.
        
        Docs: https://man7.org/linux/man-pages/man3/io_uring_submit_and_wait_reg.3.html

        Args:
            ring: io_uring structure
            cqe_ptr: Pointer to store completion queue entry
            wait_nr: Number of completions to wait for
            reg_index: Registered wait index
            
        Returns:
            Number of submitted entries, or negative error code
        """
        ...

    # Registration and utility functions
    def io_uring_register_wait_reg(ring: io_uring, reg: io_uring_reg_wait, nr: int) -> int: ...
    
    def io_uring_resize_rings(ring: io_uring, p: io_uring_params) -> int: ...
    
    def io_uring_clone_buffers_offset(
        dst: io_uring,
        src: io_uring,
        dst_off: int,
        src_off: int,
        nr: int,
        flags: int
    ) -> int: ...
    
    def io_uring_clone_buffers(dst: io_uring, src: io_uring) -> int: ...
    
    def io_uring_enable_rings(ring: io_uring) -> int: ...
    
    def io_uring_close_ring_fd(ring: io_uring) -> int: ...
    
    def io_uring_get_events(ring: io_uring) -> int: ...
    
    def io_uring_submit_and_get_events(ring: io_uring) -> int: ...
    
    def io_uring_buf_ring_head(ring: io_uring, buf_group: int, head: int) -> int: ...

    # Inline utility functions
    def io_uring_cq_advance(ring: io_uring, nr: int) -> None: ...
    
    def io_uring_cqe_seen(ring: io_uring, cqe: io_uring_cqe) -> None: ...

    # Data handling functions
    def io_uring_sqe_set_data(sqe: io_uring_sqe, obj: Any) -> None: 
        """Set user data object for a submission queue entry.
        
        Docs: https://man7.org/linux/man-pages/man3/io_uring_sqe_set_data.3.html

        Args:
            sqe: Submission queue entry
            obj: Python object to associate with this entry
        """
        ...
    
    def io_uring_cqe_get_data(cqe: io_uring_cqe) -> Any: 
        """Get user data object from a completion queue entry.
        
        Docs: https://man7.org/linux/man-pages/man3/io_uring_cqe_get_data.3.html

        Args:
            cqe: Completion queue entry
            
        Returns:
            Python object previously set with io_uring_sqe_set_data
        """
        ...
    
    def io_uring_sqe_set_data64(sqe: io_uring_sqe, data: int) -> None: 
        """Set 64-bit user data for a submission queue entry.
        
        Docs: https://man7.org/linux/man-pages/man3/io_uring_sqe_set_data64.3.html

        Args:
            sqe: Submission queue entry
            data: 64-bit integer data to associate with this entry
        """
        ...
    
    def io_uring_cqe_get_data64(cqe: io_uring_cqe) -> int: 
        """Get 64-bit user data from a completion queue entry.
        
        Docs: https://man7.org/linux/man-pages/man3/io_uring_cqe_get_data64.3.html

        Args:
            cqe: Completion queue entry
            
        Returns:
            64-bit integer data previously set with io_uring_sqe_set_data64
        """
        ...

    # SQE helper functions
    def io_uring_sqe_set_flags(sqe: io_uring_sqe, flags: int) -> None: 
        """Set flags for a submission queue entry.
        
        Docs: https://man7.org/linux/man-pages/man3/io_uring_sqe_set_flags.3.html

        Args:
            sqe: Submission queue entry
            flags: Flags to set (e.g., IOSQE_FIXED_FILE, IOSQE_ASYNC, etc.)
        """
        ...
    
    def io_uring_sqe_set_buf_group(sqe: io_uring_sqe, bgid: int) -> None: 
        """Set buffer group ID for a submission queue entry.
        
        Docs: https://man7.org/linux/man-pages/man3/io_uring_sqe_set_buf_group.3.html

        Args:
            sqe: Submission queue entry
            bgid: Buffer group ID for provided buffer operations
        """
        ...
    
    def io_uring_initialize_sqe(sqe: io_uring_sqe) -> None: 
        """Initialize a submission queue entry to default values.
        
        Args:
            sqe: Submission queue entry to initialize
        """
        ...

    # Preparation functions
    def io_uring_prep_nop(sqe: io_uring_sqe) -> None: 
        """Prepare a no-operation submission queue entry.
        
        Args:
            sqe: Submission queue entry to prepare
        """
        ...
    
    def io_uring_prep_cancel64(sqe: io_uring_sqe, user_data: int, flags: int) -> None: 
        """Prepare a cancel operation using 64-bit user data.
        
        Args:
            sqe: Submission queue entry to prepare
            user_data: User data of the operation to cancel
            flags: Cancel flags
        """
        ...
    
    def io_uring_prep_cancel(sqe: io_uring_sqe, user_data: Any, flags: int) -> None: 
        """Prepare a cancel operation.
        
        Args:
            sqe: Submission queue entry to prepare
            user_data: User data of the operation to cancel
            flags: Cancel flags
        """
        ...
    
    def io_uring_prep_cancel_fd(sqe: io_uring_sqe, fd: int, flags: int) -> None: 
        """Prepare a cancel operation for all operations on a file descriptor.
        
        Args:
            sqe: Submission queue entry to prepare
            fd: File descriptor to cancel operations for
            flags: Cancel flags
        """
        ...
    
    def io_uring_prep_waitid(
        sqe: io_uring_sqe,
        idtype: int,
        id: int,
        infop: siginfo,
        options: int,
        flags: int
    ) -> None: 
        """Prepare a waitid operation.
        
        Args:
            sqe: Submission queue entry to prepare
            idtype: Type of ID to wait for
            id: ID to wait for
            infop: Signal info structure
            options: Wait options
            flags: Additional flags
        """
        ...
    
    def io_uring_prep_fixed_fd_install(sqe: io_uring_sqe, fd: int, flags: int) -> None: 
        """Prepare a fixed file descriptor installation.
        
        Args:
            sqe: Submission queue entry to prepare
            fd: File descriptor to install
            flags: Installation flags
        """
        ...

    # Common preparation functions
    def io_uring_prep_close(sqe: io_uring_sqe, fd: int) -> None: 
        """Prepare a close operation for a file descriptor.
        
        Args:
            sqe: Submission queue entry to prepare
            fd: File descriptor to close
        """
        ...
    
    def io_uring_prep_close_direct(sqe: io_uring_sqe, file_index: int) -> None: 
        """Prepare a close operation for a direct (registered) file descriptor.
        
        Args:
            sqe: Submission queue entry to prepare
            file_index: Index of the registered file descriptor
        """
        ...
    
    def io_uring_prep_provide_buffers(
        sqe: io_uring_sqe,
        addr: memoryview,
        length: int,
        nr: int,
        bgid: int,
        bid: int = 0
    ) -> None: 
        """Prepare a buffer provision operation.
        
        Args:
            sqe: Submission queue entry to prepare
            addr: Memory view of buffer area
            length: Length of each buffer
            nr: Number of buffers to provide
            bgid: Buffer group ID
            bid: Starting buffer ID (default: 0)
        """
        ...
    
    def io_uring_prep_remove_buffers(sqe: io_uring_sqe, nr: int, bgid: int) -> None: 
        """Prepare a buffer removal operation.
        
        Args:
            sqe: Submission queue entry to prepare
            nr: Number of buffers to remove
            bgid: Buffer group ID
        """
        ...

    # File preparation functions
    def io_uring_prep_tee(
        sqe: io_uring_sqe,
        fd_in: int,
        fd_out: int,
        nbytes: int,
        splice_flags: int
    ) -> None: 
        """Prepare a tee operation (duplicate data from one pipe to another).
        
        Args:
            sqe: Submission queue entry to prepare
            fd_in: Input file descriptor (must be a pipe)
            fd_out: Output file descriptor (must be a pipe)
            nbytes: Number of bytes to duplicate
            splice_flags: Flags for the operation
        """
        ...
    
    def io_uring_prep_readv(
        sqe: io_uring_sqe,
        fd: int,
        iovecs: iovec,
        offset: int = 0
    ) -> None: 
        """Prepare a vectored read operation.
        
        Args:
            sqe: Submission queue entry to prepare
            fd: File descriptor to read from
            iovecs: I/O vector containing buffers for reading
            offset: Offset in the file (default: 0)
        """
        ...
    
    def io_uring_prep_readv2(
        sqe: io_uring_sqe,
        fd: int,
        iovecs: iovec,
        offset: int = 0,
        flags: int = 0
    ) -> None: 
        """Prepare a vectored read operation with flags.
        
        Args:
            sqe: Submission queue entry to prepare
            fd: File descriptor to read from
            iovecs: I/O vector containing buffers for reading
            offset: Offset in the file (default: 0)
            flags: Read flags (default: 0)
        """
        ...
    
    def io_uring_prep_read_fixed(
        sqe: io_uring_sqe,
        fd: int,
        buf: memoryview,
        nbytes: int,
        offset: int,
        buf_index: int
    ) -> None: 
        """Prepare a read operation using pre-registered buffers.
        
        Args:
            sqe: Submission queue entry to prepare
            fd: File descriptor to read from
            buf: Buffer memory view
            nbytes: Number of bytes to read
            offset: Offset in the file
            buf_index: Index of registered buffer
        """
        ...
    
    def io_uring_prep_writev(
        sqe: io_uring_sqe,
        fd: int,
        iovecs: iovec,
        nr_vecs: int,
        offset: int
    ) -> None: 
        """Prepare a vectored write operation.
        
        Args:
            sqe: Submission queue entry to prepare
            fd: File descriptor to write to
            iovecs: I/O vector containing data to write
            nr_vecs: Number of vectors
            offset: Offset in the file
        """
        ...
    
    def io_uring_prep_writev2(
        sqe: io_uring_sqe,
        fd: int,
        iovecs: iovec,
        nr_vecs: int,
        offset: int,
        flags: int
    ) -> None: 
        """Prepare a vectored write operation with flags.
        
        Args:
            sqe: Submission queue entry to prepare
            fd: File descriptor to write to
            iovecs: I/O vector containing data to write
            nr_vecs: Number of vectors
            offset: Offset in the file
            flags: Write flags
        """
        ...
    
    def io_uring_prep_write_fixed(
        sqe: io_uring_sqe,
        fd: int,
        buf: memoryview,
        nbytes: int,
        offset: int,
        buf_index: int
    ) -> None: 
        """Prepare a write operation using pre-registered buffers.
        
        Args:
            sqe: Submission queue entry to prepare
            fd: File descriptor to write to
            buf: Buffer memory view
            nbytes: Number of bytes to write
            offset: Offset in the file
            buf_index: Index of registered buffer
        """
        ...
    
    def io_uring_prep_fsync(
        sqe: io_uring_sqe,
        fd: int,
        fsync_flags: int = 0
    ) -> None: 
        """Prepare a file synchronization operation.
        
        Args:
            sqe: Submission queue entry to prepare
            fd: File descriptor to synchronize
            fsync_flags: Synchronization flags (default: 0)
        """
        ...
    
    def io_uring_prep_sync_file_range(
        sqe: io_uring_sqe,
        fd: int,
        length: int = 0,
        offset: int = 0,
        flags: int = 0
    ) -> None: 
        """Prepare a partial file synchronization operation.
        
        Args:
            sqe: Submission queue entry to prepare
            fd: File descriptor to synchronize
            length: Length of range to sync (default: 0 for whole file)
            offset: Offset to start sync (default: 0)
            flags: Sync flags (default: 0)
        """
        ...
    
    def io_uring_prep_openat(
        sqe: io_uring_sqe,
        path: bytes,
        flags: int = 0,
        mode: int = 0o777,
        dfd: int = -100
    ) -> None: 
        """Prepare a file open operation.
        
        Args:
            sqe: Submission queue entry to prepare
            path: Path to the file to open
            flags: Open flags (default: O_RDONLY)
            mode: File mode for new files (default: 0o777)
            dfd: Directory file descriptor (default: AT_FDCWD)
        """
        ...
    
    def io_uring_prep_openat2(
        sqe: io_uring_sqe,
        path: bytes,
        how: open_how,
        dfd: int = -100
    ) -> None: 
        """Prepare a file open operation with extended options.
        
        Args:
            sqe: Submission queue entry to prepare
            path: Path to the file to open
            how: Open specification structure
            dfd: Directory file descriptor (default: AT_FDCWD)
        """
        ...
    
    def io_uring_prep_openat_direct(
        sqe: io_uring_sqe,
        path: bytes,
        flags: int = 0,
        file_index: int = 4294967295,
        mode: int = 0o777,
        dfd: int = -100
    ) -> None: 
        """Prepare a direct (registered) file open operation.
        
        Args:
            sqe: Submission queue entry to prepare
            path: Path to the file to open
            flags: Open flags (default: O_RDONLY)
            file_index: Fixed file table index (default: auto-allocate)
            mode: File mode for new files (default: 0o777)
            dfd: Directory file descriptor (default: AT_FDCWD)
        """
        ...
    
    def io_uring_prep_openat2_direct(
        sqe: io_uring_sqe,
        path: bytes,
        how: open_how,
        file_index: int = 4294967295,
        dfd: int = -100
    ) -> None: 
        """Prepare a direct file open operation with extended options.
        
        Args:
            sqe: Submission queue entry to prepare
            path: Path to the file to open
            how: Open specification structure
            file_index: Fixed file table index (default: auto-allocate)
            dfd: Directory file descriptor (default: AT_FDCWD)
        """
        ...
    
    def io_uring_prep_read(
        sqe: io_uring_sqe,
        fd: int,
        buf: memoryview,
        nbytes: int,
        offset: int = 0
    ) -> None: 
        """Prepare a simple read operation.
        
        Args:
            sqe: Submission queue entry to prepare
            fd: File descriptor to read from
            buf: Buffer to read into
            nbytes: Number of bytes to read
            offset: Offset in the file (default: 0)
        """
        ...
    
    def io_uring_prep_read_multishot(
        sqe: io_uring_sqe,
        fd: int,
        nbytes: int,
        offset: int,
        buf_group: int
    ) -> None: 
        """Prepare a multishot read operation.
        
        Args:
            sqe: Submission queue entry to prepare
            fd: File descriptor to read from
            nbytes: Number of bytes to read
            offset: Offset in the file
            buf_group: Buffer group ID for provided buffers
        """
        ...
    
    def io_uring_prep_write(
        sqe: io_uring_sqe,
        fd: int,
        buf: memoryview,
        nbytes: int,
        offset: int
    ) -> None: 
        """Prepare a simple write operation.
        
        Args:
            sqe: Submission queue entry to prepare
            fd: File descriptor to write to
            buf: Buffer containing data to write
            nbytes: Number of bytes to write
            offset: Offset in the file
        """
        ...
    
    def io_uring_prep_files_update(
        sqe: io_uring_sqe,
        fds: List[int],
        offset: int = 0
    ) -> None: 
        """Prepare a file descriptor update operation.
        
        Args:
            sqe: Submission queue entry to prepare
            fds: List of file descriptors to update
            offset: Offset in the registered file table (default: 0)
        """
        ...
    
    def io_uring_prep_ftruncate(sqe: io_uring_sqe, fd: int, length: int) -> None: 
        """Prepare a file truncation operation.
        
        Args:
            sqe: Submission queue entry to prepare
            fd: File descriptor to truncate
            length: New file length
        """
        ...

    # Futex preparation functions
    def io_uring_prep_futex_wake(
        sqe: io_uring_sqe,
        futex: futex_state,
        val: int,
        mask: int,
        futex_flags: int
    ) -> None: ...
    
    def io_uring_prep_futex_wait(
        sqe: io_uring_sqe,
        futex: futex_state,
        val: int,
        mask: int,
        futex_flags: int
    ) -> None: ...
    
    def io_uring_prep_futex_waitv(sqe: io_uring_sqe, waiters: futex_waitv) -> None: ...

    # Helper functions
    def io_uring_put_sqe(ring: io_uring, sqe_s: io_uring_sqe) -> bool: 
        """Put submission queue entries into the ring's memory.
        
        This function copies prepared SQE entries into the ring's submission queue.
        Returns False if the queue is full and needs to be submitted first.
        
        Args:
            ring: io_uring structure
            sqe_s: Submission queue entry or entries to put
            
        Returns:
            True if successful, False if queue is full
            
        Example:
            >>> sqe = io_uring_sqe()
            >>> io_uring_prep_read(sqe, ...)
            >>> if io_uring_put_sqe(ring, sqe):
            ...     # Success, can proceed
            ... else:
            ...     # Queue full, need to submit first
            ...     io_uring_submit(ring)
            ...     io_uring_put_sqe(ring, sqe)
        """
        ...

    # OS operations
    def io_uring_prep_mkdir(sqe: io_uring_sqe, path: bytes, mode: int = 0o777) -> None: ...
    
    def io_uring_prep_mkdirat(
        sqe: io_uring_sqe, 
        path: bytes, 
        mode: int = 0o777, 
        dfd: int = -100
    ) -> None: ...
    
    def io_uring_prep_rename(sqe: io_uring_sqe, oldpath: bytes, newpath: bytes) -> None: ...
    
    def io_uring_prep_renameat(
        sqe: io_uring_sqe,
        oldpath: bytes,
        newpath: bytes,
        olddfd: int = -100,
        newdfd: int = -100,
        flags: int = 0
    ) -> None: ...
    
    def io_uring_prep_symlinkat(
        sqe: io_uring_sqe,
        target: bytes,
        linkpath: bytes,
        newdirfd: int = -100
    ) -> None: ...
    
    def io_uring_prep_symlink(sqe: io_uring_sqe, target: bytes, linkpath: bytes) -> None: ...
    
    def io_uring_prep_link(
        sqe: io_uring_sqe,
        oldpath: bytes,
        newpath: bytes,
        flags: int = 0
    ) -> None: ...
    
    def io_uring_prep_linkat(
        sqe: io_uring_sqe,
        oldpath: bytes,
        newpath: bytes,
        olddfd: int = -100,
        newdfd: int = -100,
        flags: int = 0
    ) -> None: ...
    
    def io_uring_prep_unlink(sqe: io_uring_sqe, path: bytes, flags: int = 0) -> None: ...
    
    def io_uring_prep_unlinkat(
        sqe: io_uring_sqe,
        path: bytes,
        flags: int = 0,
        dfd: int = -100
    ) -> None: ...
    
    def io_uring_prep_fallocate(
        sqe: io_uring_sqe,
        fd: int,
        length: int,
        offset: int = 0,
        mode: int = 0
    ) -> None: ...
    
    def io_uring_prep_splice(
        sqe: io_uring_sqe,
        fd_in: int,
        off_in: int,
        fd_out: int,
        off_out: int,
        nbytes: int,
        splice_flags: int
    ) -> None: ...

    # Other operations
    def io_uring_setup_buf_ring(
        ring: io_uring,
        nentries: int,
        bgid: int,
        flags: int,
        ret: int
    ) -> io_uring_buf_ring: ...
    
    def io_uring_free_buf_ring(
        ring: io_uring,
        br: io_uring_buf_ring,
        nentries: int,
        bgid: int
    ) -> int: ...
    
    def io_uring_prep_fadvise(
        sqe: io_uring_sqe,
        fd: int,
        offset: int,
        length: int,
        advice: int
    ) -> None: ...
    
    def io_uring_prep_msg_ring(
        sqe: io_uring_sqe,
        fd: int,
        length: int,
        data: int,
        flags: int = 0
    ) -> None: ...
    
    def io_uring_prep_msg_ring_fd(
        sqe: io_uring_sqe,
        fd: int,
        source_fd: int,
        target_fd: int,
        data: int,
        flags: int = 0
    ) -> None: ...
    
    def io_uring_prep_msg_ring_fd_alloc(
        sqe: io_uring_sqe,
        fd: int,
        source_fd: int,
        data: int,
        flags: int = 0
    ) -> None: ...
    
    def io_uring_prep_msg_ring_cqe_flags(
        sqe: io_uring_sqe,
        fd: int,
        length: int,
        data: int,
        cqe_flags: int,
        flags: int = 0
    ) -> None: ...
    
    def io_uring_mlock_size(entries: int, flags: int) -> int: ...
    
    def io_uring_mlock_size_params(entries: int, p: io_uring_params) -> int: ...

    # Poll operations
    def io_uring_prep_poll_add(sqe: io_uring_sqe, fd: int, poll_mask: int) -> None: ...
    
    def io_uring_prep_poll_update(
        sqe: io_uring_sqe,
        old_user_data: int,
        new_user_data: int,
        poll_mask: int,
        flags: int
    ) -> None: ...
    
    def io_uring_prep_poll_remove(sqe: io_uring_sqe, user_data: int) -> None: ...
    
    def io_uring_prep_poll_multishot(sqe: io_uring_sqe, fd: int, poll_mask: int) -> None: ...
    
    def io_uring_prep_epoll_ctl(
        sqe: io_uring_sqe,
        epfd: int,
        fd: int,
        op: int,
        ev: epoll_event
    ) -> None: ...

    # Probe operations
    def io_uring_get_probe_ring(ring: io_uring) -> io_uring_probe: ...
    
    def io_uring_get_probe() -> io_uring_probe: ...
    
    def io_uring_free_probe(probe: io_uring_probe) -> None: ...
    
    def io_uring_opcode_supported(p: io_uring_probe, op: int) -> bool: ...
    
    def io_uring_register_probe(ring: io_uring, p: io_uring_probe, nr: int) -> int: ...
    
    def probe() -> dict: ...

    # Registration operations
    def io_uring_register_buffers(ring: io_uring, iovecs: iovec, nr_iovecs: int) -> int: ...
    
    def io_uring_register_buffers_tags(
        ring: io_uring,
        iovecs: iovec,
        tags: int,
        nr: int
    ) -> int: ...
    
    def io_uring_register_buffers_sparse(ring: io_uring, nr: int) -> int: ...
    
    def io_uring_register_buffers_update_tag(
        ring: io_uring,
        off: int,
        iovecs: iovec,
        tags: int,
        nr: int
    ) -> int: ...
    
    def io_uring_unregister_buffers(ring: io_uring) -> int: ...
    
    def io_uring_register_eventfd(ring: io_uring, fd: int) -> int: ...
    
    def io_uring_register_eventfd_async(ring: io_uring, fd: int) -> int: ...
    
    def io_uring_unregister_eventfd(ring: io_uring) -> int: ...
    
    def io_uring_register_personality(ring: io_uring) -> int: ...
    
    def io_uring_unregister_personality(ring: io_uring, id: int) -> int: ...
    
    def io_uring_register_files(ring: io_uring, fds: List[int]) -> int: ...
    
    def io_uring_unregister_files(ring: io_uring) -> int: ...

    # Socket operations
    def io_uring_prep_connect(sqe: io_uring_sqe, fd: int, addr: sockaddr) -> None: ...
    
    def io_uring_prep_bind(sqe: io_uring_sqe, fd: int, addr: sockaddr) -> None: ...
    
    def io_uring_prep_listen(sqe: io_uring_sqe, fd: int, backlog: int) -> None: ...
    
    def io_uring_prep_send(
        sqe: io_uring_sqe,
        sockfd: int,
        buf: memoryview,
        length: int,
        flags: int = 0
    ) -> None: ...
    
    def io_uring_prep_recv(
        sqe: io_uring_sqe,
        sockfd: int,
        buf: memoryview,
        length: int,
        flags: int = 0
    ) -> None: ...
    
    def io_uring_prep_shutdown(sqe: io_uring_sqe, fd: int, how: int) -> None: ...

    # Statx operations
    def io_uring_prep_statx(
        sqe: io_uring_sqe,
        stat: statx,
        path: bytes,
        dfd: int = -100,
        mask: int = 0,
        flags: int = 0
    ) -> None: ...

    # Syscall operations
    def io_uring_enter(
        fd: int,
        to_submit: int,
        min_complete: int,
        flags: int,
        sig: sigset
    ) -> int: ...
    
    def io_uring_enter2(
        fd: int,
        to_submit: int,
        min_complete: int,
        flags: int,
        sig: sigset,
        sz: int
    ) -> int: ...
    
    def io_uring_setup(entries: int, p: io_uring_params) -> int: ...
    
    def io_uring_register(
        fd: int,
        opcode: int,
        arg: memoryview,
        nr_args: int
    ) -> int: ...

    # Time operations
    def io_uring_prep_timeout(
        sqe: io_uring_sqe,
        ts: timespec,
        count: int,
        flags: int
    ) -> None: ...
    
    def io_uring_prep_timeout_remove(
        sqe: io_uring_sqe,
        user_data: int,
        flags: int
    ) -> None: ...
    
    def io_uring_prep_timeout_update(
        sqe: io_uring_sqe,
        ts: timespec,
        user_data: int,
        flags: int
    ) -> None: ...
    
    def io_uring_prep_link_timeout(
        sqe: io_uring_sqe,
        ts: timespec,
        flags: int
    ) -> None: ...

    # Version operations
    def liburing_version_major() -> int: ...
    
    def liburing_version_minor() -> int: ...
    
    def liburing_version_check(major: int, minor: int) -> bool: ...
    
    def linux_version_check(version: Union[str, int, float]) -> bool: ...

    # Extended attributes operations
    def io_uring_prep_setxattr(
        sqe: io_uring_sqe,
        name: bytes,
        value: bytes,
        path: bytes,
        length: int,
        flags: int = 0
    ) -> None: ...
    
    def io_uring_prep_getxattr(
        sqe: io_uring_sqe,
        name: bytes,
        value: memoryview,
        path: bytes,
        length: int
    ) -> None: ...
    
    def io_uring_prep_fsetxattr(
        sqe: io_uring_sqe,
        fd: int,
        name: bytes,
        value: bytes,
        length: int,
        flags: int = 0
    ) -> None: ...
    
    def io_uring_prep_fgetxattr(
        sqe: io_uring_sqe,
        fd: int,
        name: bytes,
        value: memoryview,
        length: int
    ) -> None: ...

    # Queue status functions
    def io_uring_sq_ready(ring: io_uring) -> int: 
        """Get number of submission queue entries ready to be submitted.
        
        Args:
            ring: io_uring structure
            
        Returns:
            Number of entries ready for submission
        """
        ...
    
    def io_uring_sq_space_left(ring: io_uring) -> int: 
        """Get remaining space in submission queue.
        
        Args:
            ring: io_uring structure
            
        Returns:
            Number of free slots in submission queue
        """
        ...
    
    def io_uring_sqring_wait(ring: io_uring) -> int: 
        """Wait for submission queue ring to become available.
        
        Args:
            ring: io_uring structure
            
        Returns:
            0 on success, negative error code on failure
        """
        ...
    
    def io_uring_cq_ready(ring: io_uring) -> int: 
        """Get number of completion queue entries ready to be processed.
        
        Args:
            ring: io_uring structure
            
        Returns:
            Number of completed entries available
        """
        ...
    
    def io_uring_cq_has_overflow(ring: io_uring) -> bool: 
        """Check if completion queue has overflow.
        
        Args:
            ring: io_uring structure
            
        Returns:
            True if completion queue has overflow, False otherwise
        """
        ...
    
    def io_uring_cq_eventfd_enabled(ring: io_uring) -> bool: 
        """Check if eventfd is enabled for completion notifications.
        
        Args:
            ring: io_uring structure
            
        Returns:
            True if eventfd is enabled, False otherwise
        """
        ...
    
    def io_uring_cq_eventfd_toggle(ring: io_uring, enabled: bool) -> int: 
        """Toggle eventfd for completion notifications.
        
        Args:
            ring: io_uring structure
            enabled: True to enable, False to disable
            
        Returns:
            0 on success, negative error code on failure
        """
        ...

    # CQE waiting functions
    def io_uring_wait_cqe_nr(ring: io_uring, cqe_ptr: io_uring_cqe, wait_nr: int) -> int: 
        """Wait for a specific number of completion queue entries.
        
        Args:
            ring: io_uring structure
            cqe_ptr: Pointer to store completion queue entry
            wait_nr: Number of completions to wait for
            
        Returns:
            0 on success, negative error code on failure
        """
        ...
    
    def io_uring_peek_cqe(ring: io_uring, cqe_ptr: io_uring_cqe) -> int: 
        """Peek at a completion queue entry without consuming it.
        
        Args:
            ring: io_uring structure
            cqe_ptr: Pointer to store completion queue entry
            
        Returns:
            0 if entry available, -EAGAIN if no entries, negative error code on failure
        """
        ...
    
    def io_uring_wait_cqe(ring: io_uring, cqe_ptr: io_uring_cqe) -> int: 
        """Wait for a single completion queue entry.
        
        Args:
            ring: io_uring structure
            cqe_ptr: Pointer to store completion queue entry
            
        Returns:
            0 on success, negative error code on failure
        """
        ...

    # Buffer ring functions
    def io_uring_buf_ring_mask(ring_entries: int) -> int: ...
    
    def io_uring_buf_ring_init(br: io_uring_buf_ring) -> None: ...
    
    def io_uring_buf_ring_add(
        br: io_uring_buf_ring,
        addr: memoryview,
        length: int,
        bid: int,
        mask: int,
        buf_offset: int
    ) -> None: ...
    
    def io_uring_buf_ring_advance(br: io_uring_buf_ring, count: int) -> None: ...
    
    def io_uring_buf_ring_cq_advance(ring: io_uring, br: io_uring_buf_ring, count: int) -> None: ...
    
    def io_uring_buf_ring_available(ring: io_uring, br: io_uring_buf_ring, bgid: int) -> int: ...

    # SQE getting and iteration
    def io_uring_get_sqe(ring: io_uring) -> io_uring_sqe: 
        """Get a submission queue entry from the ring.
        
        This is the primary function for obtaining SQE entries to prepare operations.
        Returns None if no entries are available (queue is full).
        
        Args:
            ring: io_uring structure
            
        Returns:
            Submission queue entry, or None if queue is full
            
        Example:
            >>> sqe = io_uring_get_sqe(ring)
            >>> if sqe:
            ...     io_uring_prep_read(sqe, fd, buf, len, offset)
            ...     sqe.user_data = 123
        """
        ...
    
    def io_uring_for_each_cqe(ring: io_uring, cqe: io_uring_cqe) -> int: 
        """Iterate through all available completion queue entries.
        
        Args:
            ring: io_uring structure
            cqe: Completion queue entry for iteration
            
        Returns:
            Number of entries processed
        """
        ...
    
    _all = [
        # Core classes
        "io_uring",
        "io_uring_sqe", 
        "io_uring_cqe",
        "io_uring_params",
        "io_uring_buf_ring",
        "io_uring_reg_wait",
        "timespec",
        "siginfo",
        "sigset",
        
        # I/O and utility classes
        "iovec",
        "open_how",
        "futex_state",
        "futex_waitv",
        "sockaddr",
        "msghdr",
        "cmsghdr",
        "io_uring_recvmsg_out",
        "epoll_event",
        "io_uring_probe",
        "statx",
        
        # Queue operations
        "io_uring_queue_init_mem",
        "io_uring_queue_init_params",
        "io_uring_queue_init",
        "io_uring_queue_mmap",
        "io_uring_ring_dontfork",
        "io_uring_queue_exit",
        
        # CQE handling
        "io_uring_peek_batch_cqe",
        "io_uring_wait_cqes",
        "io_uring_wait_cqes_min_timeout",
        "io_uring_wait_cqe_timeout",
        "io_uring_wait_cqe_nr",
        "io_uring_peek_cqe",
        "io_uring_wait_cqe",
        "io_uring_cq_advance",
        "io_uring_cqe_seen",
        
        # Submission
        "io_uring_submit",
        "io_uring_submit_and_wait",
        "io_uring_submit_and_wait_timeout",
        "io_uring_submit_and_wait_min_timeout",
        "io_uring_submit_and_wait_reg",
        "io_uring_submit_and_get_events",
        
        # Registration and utility
        "io_uring_register_wait_reg",
        "io_uring_resize_rings",
        "io_uring_clone_buffers_offset",
        "io_uring_clone_buffers",
        "io_uring_enable_rings",
        "io_uring_close_ring_fd",
        "io_uring_get_events",
        "io_uring_buf_ring_head",
        
        # Data handling
        "io_uring_sqe_set_data",
        "io_uring_cqe_get_data",
        "io_uring_sqe_set_data64",
        "io_uring_cqe_get_data64",
        
        # SQE helpers
        "io_uring_sqe_set_flags",
        "io_uring_sqe_set_buf_group",
        "io_uring_initialize_sqe",
        "io_uring_get_sqe",
        "io_uring_put_sqe",
        
        # Basic preparation functions
        "io_uring_prep_nop",
        "io_uring_prep_cancel64",
        "io_uring_prep_cancel",
        "io_uring_prep_cancel_fd",
        "io_uring_prep_waitid",
        "io_uring_prep_fixed_fd_install",
        
        # Common preparation functions
        "io_uring_prep_close",
        "io_uring_prep_close_direct",
        "io_uring_prep_provide_buffers",
        "io_uring_prep_remove_buffers",
        
        # File operations
        "io_uring_prep_tee",
        "io_uring_prep_readv",
        "io_uring_prep_readv2",
        "io_uring_prep_read_fixed",
        "io_uring_prep_writev",
        "io_uring_prep_writev2",
        "io_uring_prep_write_fixed",
        "io_uring_prep_fsync",
        "io_uring_prep_sync_file_range",
        "io_uring_prep_openat",
        "io_uring_prep_openat2",
        "io_uring_prep_openat_direct",
        "io_uring_prep_openat2_direct",
        "io_uring_prep_read",
        "io_uring_prep_read_multishot",
        "io_uring_prep_write",
        "io_uring_prep_files_update",
        "io_uring_prep_ftruncate",
        
        # Futex operations
        "io_uring_prep_futex_wake",
        "io_uring_prep_futex_wait",
        "io_uring_prep_futex_waitv",
        
        # OS operations
        "io_uring_prep_mkdir",
        "io_uring_prep_mkdirat",
        "io_uring_prep_rename",
        "io_uring_prep_renameat",
        "io_uring_prep_symlinkat",
        "io_uring_prep_symlink",
        "io_uring_prep_link",
        "io_uring_prep_linkat",
        "io_uring_prep_unlink",
        "io_uring_prep_unlinkat",
        "io_uring_prep_fallocate",
        "io_uring_prep_splice",
        
        # Other operations
        "io_uring_setup_buf_ring",
        "io_uring_free_buf_ring",
        "io_uring_prep_fadvise",
        "io_uring_prep_msg_ring",
        "io_uring_prep_msg_ring_fd",
        "io_uring_prep_msg_ring_fd_alloc",
        "io_uring_prep_msg_ring_cqe_flags",
        "io_uring_mlock_size",
        "io_uring_mlock_size_params",
        
        # Poll operations
        "io_uring_prep_poll_add",
        "io_uring_prep_poll_update",
        "io_uring_prep_poll_remove",
        "io_uring_prep_poll_multishot",
        "io_uring_prep_epoll_ctl",
        
        # Probe operations
        "io_uring_get_probe_ring",
        "io_uring_get_probe",
        "io_uring_free_probe",
        "io_uring_opcode_supported",
        "io_uring_register_probe",
        "probe",
        
        # Registration operations
        "io_uring_register_buffers",
        "io_uring_register_buffers_tags",
        "io_uring_register_buffers_sparse",
        "io_uring_register_buffers_update_tag",
        "io_uring_unregister_buffers",
        "io_uring_register_eventfd",
        "io_uring_register_eventfd_async",
        "io_uring_unregister_eventfd",
        "io_uring_register_personality",
        "io_uring_unregister_personality",
        "io_uring_register_files",
        "io_uring_unregister_files",
        
        # Socket operations
        "io_uring_prep_connect",
        "io_uring_prep_bind",
        "io_uring_prep_listen",
        "io_uring_prep_send",
        "io_uring_prep_recv",
        "io_uring_prep_shutdown",
        
        # Statx operations
        "io_uring_prep_statx",
        
        # Syscall operations
        "io_uring_enter",
        "io_uring_enter2",
        "io_uring_setup",
        "io_uring_register",
        
        # Time operations
        "io_uring_prep_timeout",
        "io_uring_prep_timeout_remove",
        "io_uring_prep_timeout_update",
        "io_uring_prep_link_timeout",
        
        # Version operations
        "liburing_version_major",
        "liburing_version_minor",
        "liburing_version_check",
        "linux_version_check",
        
        # Extended attributes operations
        "io_uring_prep_setxattr",
        "io_uring_prep_getxattr",
        "io_uring_prep_fsetxattr",
        "io_uring_prep_fgetxattr",
        
        # Queue status functions
        "io_uring_sq_ready",
        "io_uring_sq_space_left",
        "io_uring_sqring_wait",
        "io_uring_cq_ready",
        "io_uring_cq_has_overflow",
        "io_uring_cq_eventfd_enabled",
        "io_uring_cq_eventfd_toggle",
        
        # Buffer ring functions
        "io_uring_buf_ring_mask",
        "io_uring_buf_ring_init",
        "io_uring_buf_ring_add",
        "io_uring_buf_ring_advance",
        "io_uring_buf_ring_cq_advance",
        "io_uring_buf_ring_available",
        
        # Iteration functions
        "io_uring_for_each_cqe",
    ]
else:
    _all = []
__all__ = _all + ['_all']