"""Original Vietnamese interview scripts. Edit here, then run scripts/build.py."""

CARDS = []


def add(id, group, title, cue, script, follow, trap, *, priority=True, kind="theory", minutes=2, extra="", refs=()):
    CARDS.append(dict(id=id, group=group, title=title, cue=cue, script=script.strip(),
                      follow=follow, trap=trap, priority=priority, kind=kind,
                      minutes=minutes, extra=extra, refs=refs))


add("oop", "OOP & Patterns", "Bốn tính chất OOP là gì?", "Bảo vệ trạng thái → hợp đồng → thay thế implementation", """
Theo em, OOP tổ chức chương trình quanh đối tượng có trạng thái và hành vi. Bốn tính chất chính là đóng gói, trừu tượng, kế thừa và đa hình. Điều quan trọng là giải thích chúng giúp bảo vệ nghiệp vụ và thay đổi code như thế nào.

Đóng gói nghĩa là kiểm soát việc thay đổi trạng thái. Ví dụ, Wallet không cho bên ngoài tùy ý set số dư; thao tác giữ tiền phải kiểm tra số tiền dương và số dư khả dụng. Trừu tượng là đưa ra hợp đồng cần dùng, chẳng hạn BankConnector có thao tác chuyển tiền và truy vấn trạng thái, còn chi tiết HTTP và chữ ký nằm bên trong.

Kế thừa thể hiện quan hệ is-a và cho phép tái sử dụng phần phù hợp của lớp cha. Đa hình cho phép service gọi cùng một interface nhưng chạy implementation của các ngân hàng khác nhau. Service không cần tự chứa toàn bộ điều kiện riêng của từng ngân hàng.

Em không xem getter và setter là đủ để có đóng gói tốt. Nếu setter cho phép object rơi vào trạng thái sai thì nghiệp vụ vẫn chưa được bảo vệ. Em cũng ưu tiên composition khi mục tiêu là lắp ghép hoặc thay thế hành vi, tránh cây kế thừa quá sâu gây phụ thuộc khó kiểm soát.
""", [("Đóng gói và trừu tượng khác nhau thế nào?", "Đóng gói kiểm soát trạng thái và quyền truy cập implementation; trừu tượng chọn hợp đồng cần thể hiện, bỏ qua chi tiết không cần cho bên sử dụng.")], "Đừng chỉ đọc bốn định nghĩa; luôn gắn với Wallet hoặc BankConnector.")

add("interface", "OOP & Patterns", "Interface, abstract class và composition khác nhau thế nào?", "Hợp đồng → phần chung thực sự → tránh kế thừa ép buộc", """
Em dùng interface khi cần mô tả một khả năng hoặc hợp đồng mà nhiều implementation có thể thực hiện. Abstract class phù hợp khi các lớp có quan hệ gần nhau và cần chia sẻ trạng thái hoặc một phần thuật toán. Một class implement được nhiều interface nhưng chỉ extends một class.

Ví dụ, em định nghĩa BankConnector để service phụ thuộc hợp đồng chung. Mỗi connector nhận HTTP client, signer và mapper qua constructor. Đây là composition: object được tạo từ các thành phần cộng tác, nên có thể thay từng thành phần và test độc lập.

Nếu mọi ngân hàng thực sự có cùng một bộ khung thuật toán ổn định, em có thể cân nhắc abstract class hoặc Template Method. Tuy nhiên, nếu ngân hàng nào cũng phải override nhiều bước và thêm ngoại lệ, đó là dấu hiệu phần trừu tượng đang bị ép.

Từ Java 8, interface có default method, nhưng không vì thế thay thế hoàn toàn abstract class. Em lựa chọn từ mức độ thay đổi và hợp đồng, không từ mong muốn giảm vài dòng code. Khi chưa có nhu cầu rõ, một implementation đơn giản thường dễ bảo trì hơn một hierarchy nhiều tầng.
""", [("Khi nào inheritance vi phạm thiết kế?", "Khi lớp con không giữ được hợp đồng của lớp cha hoặc phải vô hiệu hóa hành vi mà bên dùng đang dựa vào; đó cũng là vấn đề Liskov substitution.")], "Tái sử dụng code không đủ để kết luận nên dùng inheritance.")

add("solid", "OOP & Patterns", "Giải thích SOLID bằng module tích hợp ngân hàng", "Mỗi nguyên tắc → một quyết định cụ thể", """
Em hiểu SOLID là các nguyên tắc giúp code dễ thay đổi và kiểm thử. Với Single Responsibility, em tách orchestration giao dịch, giao tiếp ngân hàng và persistence vì chúng có những lý do thay đổi khác nhau.

Open/Closed nghĩa là mở rộng được hành vi mà hạn chế sửa phần ổn định. Khi thêm ngân hàng, em thêm connector và cấu hình đăng ký thay vì sửa if-else ở nhiều service. Liskov Substitution yêu cầu implementation giữ đúng hợp đồng: nếu accepted chỉ là đã tiếp nhận, connector không được trả accepted với ý nghĩa đã chuyển tiền xong.

Interface Segregation giúp interface vừa với bên dùng. Ngân hàng chỉ hỗ trợ transfer không nên bị ép implement refund. Dependency Inversion nghĩa là policy nghiệp vụ phụ thuộc abstraction, không gắn trực tiếp với SDK cụ thể; implementation được cung cấp từ bên ngoài.

Em không hiểu SOLID là mỗi class chỉ có một method hay mọi class phải có interface. Abstraction chỉ đáng giá khi phản ánh trách nhiệm hoặc điểm thay đổi thật. Trade-off của tách quá nhỏ là phải đi qua nhiều lớp mới hiểu được một luồng đơn giản.
""", [("DI và DIP có giống nhau không?", "DIP là nguyên tắc về hướng phụ thuộc. DI là kỹ thuật cung cấp dependency từ bên ngoài; dùng Spring inject một concrete class chưa tự chứng minh thiết kế đã theo DIP.")], "Đừng chỉ mở rộng năm chữ cái mà không có ví dụ.")

add("strategy", "OOP & Patterns", "Strategy, Factory và Adapter phối hợp ra sao?", "Chọn hành vi • cung cấp object • chuyển hợp đồng", """
Ba pattern này giải quyết ba vấn đề khác nhau. Strategy cho phép thay thế thuật toán hoặc hành vi qua một hợp đồng chung. Factory đóng gói việc tạo hoặc cung cấp object. Adapter chuyển một interface bên ngoài sang hợp đồng mà hệ thống mình sử dụng.

Trong bài tích hợp ngân hàng, mỗi BankConnector chuyển request nội bộ sang payload của ngân hàng, ký và map response về kiểu chung; đây là vai trò Adapter. Ở tầng orchestration, việc sử dụng các connector có thể thay thế nhau mang tính Strategy. Registry hoặc factory cung cấp connector phù hợp theo bank code.

Ví dụ, TransferService chỉ yêu cầu connector gửi giao dịch với mã tham chiếu ổn định. Nó không biết ngân hàng A dùng JSON hay ngân hàng B dùng XML. Khi thêm ngân hàng, em thêm implementation và kiểm thử hợp đồng, thay vì đưa chi tiết giao thức vào service.

Em vẫn giữ các khác biệt nghiệp vụ thật, chẳng hạn ngân hàng không hỗ trợ inquiry hoặc có trạng thái bất đồng bộ riêng. Chuẩn hóa không có nghĩa là che mất thông tin cần cho recovery. Em cũng không gọi mọi hàm trả về object là Factory Method; tên pattern cần phù hợp cấu trúc thực tế.
""", [("Có cần cả ba pattern mọi lúc không?", "Không. Một registry do dependency injection cung cấp có thể đủ; chỉ thêm factory khi có logic lựa chọn hoặc khởi tạo cần đóng gói.")], "Đừng trộn Factory là chọn object với Strategy là thay hành vi.")

add("singleton", "OOP & Patterns", "Singleton có thread-safe không? Spring singleton là gì?", "Một instance ≠ trạng thái an toàn ≠ một instance toàn cluster", """
Singleton kiểm soát số instance của một class trong phạm vi nhất định và cung cấp điểm truy cập. Trong Java có thể triển khai bằng eager initialization, static holder hoặc enum. Với lazy double-checked locking, cần đồng bộ đúng và dùng volatile cho reference.

Em tách hai vấn đề: tạo instance an toàn và sử dụng instance an toàn. Dù khởi tạo thread-safe, một singleton có field mutable mà nhiều thread cùng sửa vẫn có race condition. Ví dụ, service giữ currentUser hoặc currentTransfer ở field sẽ làm dữ liệu giữa các request ảnh hưởng nhau.

Spring singleton mặc định là một instance cho mỗi bean definition trong một container. Khi ứng dụng chạy nhiều pod, mỗi container vẫn có bean riêng. Vì thế em thường thiết kế service stateless, giữ dữ liệu request ở biến cục bộ và quản lý dữ liệu chia sẻ tại tầng phù hợp.

Em không dùng Singleton làm cơ chế bảo đảm chỉ có một lệnh trừ tiền trong toàn hệ thống. Invariant số dư cần được bảo vệ ở database hoặc ledger service có cơ chế concurrency rõ ràng. Global state cũng làm test khó cô lập, nên em ưu tiên dependency injection hơn việc gọi singleton tĩnh ở khắp nơi.
""", [("Tại sao double-checked locking cần volatile?", "Để việc công bố reference có bảo đảm visibility và ordering cần thiết; tránh thread khác quan sát một object chưa được công bố an toàn.")], "Thread-safe construction không đồng nghĩa thread-safe business logic.")

add("other-patterns", "OOP & Patterns", "State, Builder, Observer và Template Method dùng khi nào?", "Nói vấn đề trước → pattern sau", """
State hữu ích khi hành vi phụ thuộc trạng thái và các quy tắc chuyển trạng thái đủ phức tạp. Với giao dịch, em xác định trạng thái nào được phép chuyển, sự kiện nào kích hoạt và tác động nào chỉ thực hiện một lần. Nếu đơn giản, enum cùng bảng transition có thể đủ, chưa cần một class cho mỗi trạng thái.

Builder giúp tạo object có nhiều tham số, nhất là object immutable. Nhưng builder vẫn phải validate trường bắt buộc và tổ hợp giá trị, chẳng hạn amount dương và currency hợp lệ. Nó không tự bảo đảm nghiệp vụ đúng.

Observer mô tả bên đăng ký nhận thông báo về thay đổi. Em phân biệt notification trong cùng process với event qua broker: messaging phân tán có thêm delivery, duplicate, ordering và recovery. Template Method định nghĩa bộ khung thuật toán ở lớp cha và để lớp con thay một số bước.

Ví dụ, sau khi giao dịch thành công, một event có thể kích hoạt thông báo. Tuy nhiên, em không để lỗi gửi SMS rollback giao dịch tiền đã hoàn tất. Trade-off chung là pattern thêm cấu trúc và indirection, nên cần lợi ích rõ về thay đổi hoặc kiểm thử.
""", [("State khác Strategy ở đâu?", "Strategy thường là lựa chọn cách thực hiện hành vi; State mô hình hóa hành vi và chuyển đổi theo trạng thái của object. Chúng có thể có cấu trúc tương tự nhưng ý định khác.")], "Không cần thuộc toàn bộ danh mục GoF trước khi hiểu nhóm pattern cốt lõi.", priority=False)

add("jmm", "Java & Concurrency", "JMM, volatile, synchronized và atomic khác nhau thế nào?", "Visibility • atomicity • ordering • phạm vi JVM", """
Java Memory Model mô tả những bảo đảm khi thread đọc và ghi bộ nhớ chia sẻ. Em phân biệt visibility, tức nhìn thấy thay đổi; atomicity, tức thao tác không bị xen ngang gây sai kết quả; và ordering, tức những ràng buộc về thứ tự có thể quan sát.

volatile cung cấp bảo đảm visibility và ordering thông qua happens-before, nhưng không biến một chuỗi đọc-sửa-ghi thành nguyên tử. count++ vẫn có thể mất cập nhật. synchronized bảo vệ vùng critical section giữa các thread dùng cùng monitor và có bảo đảm visibility khi nhả và lấy khóa.

AtomicInteger cung cấp thao tác nguyên tử trên một biến, ví dụ incrementAndGet hoặc compareAndSet. Em có thể dùng volatile cho cờ dừng, atomic cho bộ đếm, và lock khi cần giữ invariant trên nhiều giá trị liên quan. Với cập nhật nhiều field, từng field atomic riêng chưa đủ để toàn bộ trạng thái nhất quán.

Các cơ chế này chỉ giải quyết concurrency trong JVM. Nếu hai pod cùng trừ số dư trong database, synchronized tại một pod không bảo vệ được pod còn lại. Lúc đó em cần transaction, constraint hoặc cơ chế phối hợp tại nơi dữ liệu được quản lý.
""", [("Happens-before có phải thứ tự thời gian thực không?", "Nó là quan hệ bảo đảm về visibility và ordering giữa các hành động, không đơn giản là quan sát đồng hồ thấy thao tác A chạy trước B.")], "Đừng giải thích volatile bằng câu tuyệt đối 'bỏ qua CPU cache'.", refs=("java-concurrency",))

add("collections", "Java & Concurrency", "HashMap và ConcurrentHashMap: khi nào dùng?", "equals/hashCode → mutable key → thao tác ghép", """
HashMap ánh xạ key đến value dựa trên hash và kiểm tra equals khi cần phân biệt key. Hai object bằng nhau theo equals phải có cùng hashCode. Nếu dùng một field mutable để tính hash rồi sửa field sau khi đưa key vào map, việc tra cứu có thể không tìm lại được entry như mong muốn.

Em dùng HashMap khi dữ liệu được giới hạn trong một thread hoặc được đồng bộ đúng ở bên ngoài. ConcurrentHashMap phù hợp khi nhiều thread cùng truy cập và cập nhật map, nhưng em vẫn phải nhìn vào tính nguyên tử của thao tác nghiệp vụ.

Ví dụ, containsKey rồi put là hai thao tác riêng. Nếu muốn thêm khi chưa có, em dùng putIfAbsent; nếu cần cập nhật theo giá trị hiện tại, có thể dùng compute với phần xử lý ngắn và tránh tác vụ blocking không cần thiết. ConcurrentHashMap không chấp nhận null key hoặc value.

Map thread-safe cũng không tự làm object mutable bên trong thread-safe. Nếu value là một danh sách bị nhiều thread sửa, em vẫn cần thiết kế riêng. Và map trong memory không thay thế database unique constraint để chống giao dịch trùng giữa nhiều instance hoặc sau restart.
""", [("Có thể dùng ConcurrentHashMap làm idempotency store không?", "Chỉ là lớp tối ưu cục bộ trong phạm vi hạn chế; không đủ làm bảo đảm bền vững vì mỗi instance có map riêng và dữ liệu mất khi process dừng.")], "Thread-safe từng method không đồng nghĩa cả chuỗi nghiệp vụ atomic.")

add("money-java", "Java & Concurrency", "Vì sao không dùng double cho tiền?", "Biểu diễn chính xác → scale → rounding → hợp đồng", """
double biểu diễn số thực nhị phân nên nhiều giá trị thập phân không được thể hiện chính xác. Với tiền, sai số tích lũy hoặc làm tròn không nhất quán có thể gây lệch dữ liệu. Em thường dùng BigDecimal hoặc integer biểu diễn đơn vị tiền nhỏ nhất, tùy hợp đồng dữ liệu và phạm vi giá trị.

Với BigDecimal, em ưu tiên khởi tạo từ chuỗi thập phân hoặc dữ liệu đã được chuẩn hóa, tránh new BigDecimal từ một double đã mang sai số. Em định nghĩa currency, scale và quy tắc rounding rõ ràng, nhất là khi chia phí, tính tỷ lệ hoặc đổi tiền.

Ví dụ, 1.0 và 1.00 có thể so sánh bằng nhau qua compareTo, nhưng equals còn xét scale. Nếu dùng làm key hoặc so sánh trong test, em cần biết khác biệt đó. BigDecimal cũng immutable: phép cộng tạo giá trị mới, không sửa object cũ.

Trade-off của integer là phải thống nhất đơn vị và kiểm soát overflow. Trade-off của BigDecimal là cần quản lý scale, precision và serialization chặt chẽ. Em không làm tròn tùy ý ở mọi bước; quy tắc phải được nghiệp vụ xác nhận và dùng nhất quán giữa service, database và ngân hàng.
""", [("Có phải mọi loại tiền đều có hai chữ số thập phân?", "Không. Đơn vị và số chữ số phải theo currency và hợp đồng nghiệp vụ, không hard-code mặc định cho mọi loại tiền.")], "Đừng dùng số tiền kiểu chuỗi mà không validate, hoặc dùng float ở frontend rồi xem đó là nguồn sự thật.")

add("heap-gc", "Java & Concurrency", "Heap, stack, memory leak và G1/ZGC", "Đo allocation/pause/live set trước khi đổi collector", """
Stack gắn với việc thực thi method của từng thread, gồm frame và biến cục bộ; heap là vùng quản lý object theo mô hình JVM. Em tách phần này với JMM, vốn nói về hành vi truy cập bộ nhớ giữa các thread. Chi tiết tối ưu runtime có thể thay đổi cách cấp phát thực tế.

Có GC vẫn có thể memory leak theo nghĩa ứng dụng giữ object không còn cần thiết nhưng vẫn reachable. Ví dụ là cache không giới hạn, listener không được gỡ hoặc ThreadLocal không được dọn khi dùng thread pool. GC không biết object đó đã vô ích về mặt nghiệp vụ.

Khi điều tra, em xem heap usage sau GC, allocation rate, pause time và GC log, rồi dùng heap dump hoặc profiler khi phù hợp. Em phân biệt heap với native memory và thread stacks; tăng Xmx không giải quyết mọi loại hết bộ nhớ.

Về collector, G1 hướng đến cân bằng throughput và latency, còn ZGC ưu tiên pause thấp với đánh đổi tài nguyên tùy workload. Em xác nhận phiên bản JDK và đo p95, p99, CPU, memory trước và sau. Đổi collector không thay thế việc sửa leak hoặc giảm cấp phát quá mức.
""", [("CPU thấp nhưng latency cao có phải GC không?", "Có thể, nhưng cần kiểm tra cả lock, connection pool, downstream và queue time. Không kết luận từ một metric.")], "Không đồng nhất heap/stack/GC với toàn bộ Java Memory Model.", priority=False, refs=("gc",))

add("thread-pool", "Java & Concurrency", "Thiết kế ExecutorService gọi API ngân hàng", "Bounded threads + bounded queue + timeout + bulkhead", """
Thread pool tái sử dụng worker và kiểm soát concurrency. Em bắt đầu từ loại workload, traffic, latency downstream và giới hạn connection; không chọn pool size chỉ vì một con số quen thuộc. CPU-bound thường bị giới hạn bởi CPU, còn gọi ngân hàng chủ yếu phải chờ I/O.

newFixedThreadPool dùng queue không giới hạn theo cấu hình factory mặc định, nên khi ngân hàng chậm có thể tích tụ công việc. newCachedThreadPool có thể tạo rất nhiều thread. Em thường cấu hình ThreadPoolExecutor với giới hạn thread, queue và rejection policy rõ ràng. ScheduledExecutorService phù hợp với tác vụ định thời trong process, nhưng không thay durable scheduler nếu công việc phải tồn tại qua restart.

Em kết hợp timeout ở HTTP client, connection pool phù hợp và giới hạn riêng theo ngân hàng để một bên chậm không chiếm hết tài nguyên. Khi queue đầy, hành vi từ chối phải phản ánh đúng hợp đồng: request chưa được nhận bền vững khác với giao dịch đã được nhận và đang chờ.

Trade-off là queue lớn hấp thụ burst nhưng tăng thời gian chờ. Em đo queue age, rejected tasks, active threads và downstream latency. Tăng thread chỉ hữu ích nếu tài nguyên phía sau còn khả năng phục vụ.
""", [("CallerRunsPolicy có luôn tốt không?", "Không. Nó tạo backpressure bằng cách chạy trên thread gọi, nhưng có thể chặn request thread hoặc event loop; cần xem ngữ cảnh thực thi.")], "Không dùng unbounded queue như giải pháp scale.")

add("virtual-threads", "Java & Concurrency", "Vì sao dùng virtual threads trong Java 21?", "Nhiều tác vụ chờ I/O • không tăng tốc CPU • vẫn giới hạn downstream", """
Virtual thread là thread nhẹ được JVM quản lý và chạy trên các platform thread. Nó giúp mô hình một thread cho một tác vụ có thể phục vụ nhiều công việc chờ I/O mà không cần tương ứng từng ấy OS thread. Lợi ích chính là khả năng xử lý đồng thời, không phải làm một phép tính chạy nhanh hơn.

Ví dụ, API cần chờ nhiều lời gọi ngân hàng có thể giữ cách viết blocking dễ hiểu với virtual threads. Nhưng nếu database chỉ có một số connection hữu hạn hoặc ngân hàng chỉ chấp nhận một mức tải nhất định, virtual threads không xóa được giới hạn đó. Em vẫn dùng semaphore, rate limit, deadline và connection pool.

Em không tạo pool virtual threads chỉ để tái sử dụng như platform threads; thường tạo theo task và giới hạn tài nguyên khan hiếm riêng. Em cũng xem mức sử dụng ThreadLocal và chi phí bộ nhớ khi số lượng task lớn.

Riêng Java 21, blocking trong một số ngữ cảnh như synchronized có thể pin carrier thread; cần kiểm tra đúng phiên bản, library và đo workload. JD dùng Java 8 trở lên nên em sẽ hỏi runtime hiện tại trước khi đề xuất chuyển. Em không xem virtual threads là thay thế mọi mô hình async hoặc reactive.
""", [("Có tăng tốc công việc CPU-bound không?", "Không làm CPU có thêm năng lực tính toán; cần giới hạn parallelism theo tài nguyên CPU thực tế.")], "Lưu ý pinning được cải thiện ở các JDK sau; không khái quát hạn chế Java 21 cho mọi phiên bản.", priority=False, refs=("virtual",))

add("futures", "Java & Concurrency", "thenApply, thenCompose và thenCombine khác nhau thế nào?", "Biến đổi giá trị • nối bước phụ thuộc • ghép hai kết quả", """
CompletableFuture cho phép biểu diễn kết quả bất đồng bộ và ghép các bước xử lý. thenApply biến đổi một giá trị thành giá trị khác. thenCompose dùng khi bước tiếp theo trả về một future và phụ thuộc kết quả trước đó; nó giúp tránh future lồng nhau.

Ví dụ, em lấy tài khoản rồi dùng tài khoản đó gọi kiểm tra điều kiện qua API khác. Bước sau phụ thuộc dữ liệu bước trước nên dùng thenCompose. Ngược lại, lấy hồ sơ khách hàng và cấu hình ngân hàng là hai tác vụ độc lập; em có thể khởi chạy cả hai rồi dùng thenCombine để ghép kết quả.

Em không mặc định mọi callback đều chạy trên thread mới. Biến thể không có Async có thể chạy trên thread hoàn thành future; biến thể Async cần xem executor, và nếu không cung cấp thì thường dùng common pool. Với blocking I/O, em chọn executor phù hợp và tránh chiếm tài nguyên dùng chung ngoài ý muốn.

Trade-off là chain quá dài hoặc join tùy tiện có thể khó đọc và vô tình chặn thread. Em chỉ song song hóa các bước độc lập; nghiệp vụ cần thứ tự hoặc cùng transaction không được tách async chỉ để có vẻ nhanh hơn.
""", [("thenCombine có tự khởi chạy hai tác vụ không?", "Không. Nó kết hợp các stage đã có; cách tạo và lập lịch từng tác vụ quyết định việc chúng có chạy đồng thời hay không.")], "Không truyền transaction hoặc ThreadLocal sang executor theo giả định tự động.", refs=("future",))

add("future-errors", "Java & Concurrency", "Xử lý exception và timeout với CompletableFuture", "Phục hồi có chủ đích → giữ ý nghĩa lỗi → hủy không đồng nghĩa dừng I/O", """
Em tách quan sát kết quả với phục hồi lỗi. exceptionally xử lý nhánh lỗi và có thể trả giá trị thay thế. handle nhận cả kết quả lẫn exception để chuyển thành kết quả mới. whenComplete chủ yếu phù hợp cho quan sát hoặc cleanup; callback này vẫn có thể gây lỗi nếu chính nó ném exception.

Trong payment, em không trả một giá trị thành công giả từ exceptionally chỉ để chain tiếp tục. Ví dụ, timeout ngân hàng phải được giữ là kết quả chưa xác định, khác với ngân hàng xác nhận từ chối. Em phân loại exception và giữ correlation ID để truy vết.

Về timeout, em đặt deadline tổng và timeout cho I/O bên dưới. Hết thời gian chờ một future không chứng minh HTTP request đã dừng hoặc ngân hàng chưa xử lý. cancel cũng không tự bảo đảm tác động bên ngoài được hủy. Java 8 và các JDK mới hơn có API timeout khác nhau nên cần chọn đúng runtime.

Trade-off của fallback là có thể che lỗi hoặc làm dữ liệu không chính xác. Em chỉ fallback khi ý nghĩa nghiệp vụ cho phép, ví dụ dùng cấu hình cache còn hợp lệ; không fallback một lệnh chuyển tiền chưa rõ kết quả thành thất bại chắc chắn rồi tự hoàn tiền.
""", [("join khác get ở điểm nào đáng chú ý?", "Cả hai đều có thể chờ; chúng khác cách biểu diễn exception và get có biến thể chờ có timeout. Không đặt chúng tùy tiện trên thread cần giữ non-blocking.")], "CompletableFuture không tự hủy một giao dịch ngân hàng.", refs=("future",))

add("locks", "Java & Concurrency", "Deadlock, ReentrantLock và ThreadLocal", "Lock ordering • cleanup finally • không để state request trên singleton", """
Deadlock xảy ra khi các thread giữ tài nguyên và chờ nhau theo chu trình mà không thể tiếp tục. Ví dụ, thread A khóa tài khoản 1 rồi chờ 2, còn thread B khóa 2 rồi chờ 1. Em giảm nguy cơ bằng thứ tự lấy khóa nhất quán và vùng khóa ngắn.

ReentrantLock cung cấp thêm lựa chọn như tryLock và lấy khóa có thể bị interrupt; synchronized đơn giản và tự nhả monitor khi rời block. Nếu dùng lock thủ công, em unlock trong finally. Timeout lấy khóa giúp kiểm soát chờ, nhưng không thay thế thiết kế tránh chu trình.

Khi điều tra, em lấy thread dump và xem thread state, stack cùng các lock đang chờ; với deadlock database thì xem lock và transaction phía database. Không phải mọi thread WAITING đều là lỗi, vì chờ task hoặc chờ I/O có thể là bình thường.

ThreadLocal giữ dữ liệu theo thread, không tự theo request qua executor. Với thread pool, phải cleanup khi kết thúc để tránh rò dữ liệu hoặc giữ object lâu. Em không đặt currentUser hay currentTransfer trong field của Spring singleton. Trade-off của shared mutable state là làm reasoning và test concurrency khó hơn đáng kể.
""", [("synchronized fair không?", "Không có bảo đảm fairness như lựa chọn fair của ReentrantLock; fairness cũng có chi phí và không tự bảo đảm SLA nghiệp vụ.")], "JVM lock không phải distributed lock.")
add("transactions", "Spring & Database", "@Transactional hoạt động ra sao, rollback được đến đâu?", "Proxy → local transaction → rollback rules → external side effects", """
Trong cách dùng Spring phổ biến, proxy bao quanh lời gọi method để bắt đầu hoặc tham gia transaction, rồi commit hoặc rollback theo kết quả và cấu hình. Em xác định transaction manager đang quản lý tài nguyên nào, thường là database, thay vì hiểu annotation bao phủ mọi tác động trong method.

Nếu method vừa ghi database vừa gọi ngân hàng, rollback database không tự đảo ngược giao dịch đã xảy ra ở ngân hàng. Vì vậy, em dùng local transaction ngắn cho các thay đổi nội bộ cần nguyên tử, kết hợp trạng thái bền vững và recovery cho giao tiếp bên ngoài.

Trong proxy mode, self-invocation không đi qua proxy: một method gọi method khác trên chính object không làm annotation của method trong được áp dụng như một lời gọi qua proxy. Nếu method ngoài đã có transaction, method trong vẫn có thể chạy trong transaction đó; vấn đề là annotation riêng của nó không được intercept.

Với cấu hình mặc định truyền thống của Spring, RuntimeException và Error gây rollback, checked exception thì cần xem rule. Nếu catch lỗi rồi không để proxy thấy hoặc không đánh dấu rollback, transaction có thể commit. Em viết test rollback thật và kiểm tra runtime/config, tránh coi annotation là bảo đảm tự động cho mọi trường hợp.
""", [("Có giữ transaction lúc gọi HTTP ngân hàng không?", "Em tránh nếu có thể vì giữ lock và connection trong lúc chờ mạng. Tách bước phải đi kèm state machine, idempotency và recovery; chỉ bỏ annotation là chưa đủ.")], "Local rollback không phải distributed rollback.", refs=("spring-tx",))

add("propagation", "Spring & Database", "REQUIRED, REQUIRES_NEW và rollback-only", "Cùng physical transaction hay transaction độc lập?", """
Propagation xác định method tham gia transaction hiện có như thế nào. REQUIRED tham gia transaction đang chạy hoặc tạo mới nếu chưa có. REQUIRES_NEW tạo transaction độc lập và tạm ngưng transaction bên ngoài khi transaction manager hỗ trợ.

Ví dụ, method ngoài gọi qua bean khác sang method dùng REQUIRES_NEW. Nếu method trong commit, rồi method ngoài rollback, dữ liệu đã commit ở transaction trong không tự mất. Điều này có thể phù hợp cho một số bản ghi vận hành, nhưng nguy hiểm nếu bản ghi đó khẳng định một nghiệp vụ chưa thực sự hoàn tất.

Nếu dùng REQUIRED và một nhánh đánh dấu transaction rollback-only, việc bắt exception ở bên ngoài không nhất thiết xóa được trạng thái đó; khi commit có thể gặp UnexpectedRollbackException. Em xem ranh giới proxy và nguyên nhân rollback thay vì chỉ thêm try-catch.

Trade-off của REQUIRES_NEW là có thể cần thêm connection trong khi transaction ngoài vẫn giữ tài nguyên, gây áp lực pool hoặc chờ lock. NESTED nếu được hỗ trợ thường liên quan savepoint, không giống transaction độc lập. Em chọn propagation từ yêu cầu nhất quán, không dùng REQUIRES_NEW như cách làm cho lỗi biến mất.
""", [("Gọi REQUIRES_NEW bằng this.method() có tác dụng không?", "Trong proxy mode thông thường, self-invocation bỏ qua interceptor nên không tạo transaction mới theo annotation của method đó.")], "Một transaction commit độc lập có thể làm dữ liệu phản ánh sai nghiệp vụ tổng thể.")

add("isolation", "Spring & Database", "READ_COMMITTED, REPEATABLE_READ và SERIALIZABLE", "Invariant trước → anomaly → cơ chế DB → đo contention", """
Isolation mô tả mức độ các transaction đồng thời được nhìn thấy và ảnh hưởng lẫn nhau. READ_COMMITTED ngăn dirty read, nhưng hai lần đọc có thể thấy dữ liệu đã commit khác nhau. REPEATABLE_READ tăng bảo đảm cho việc đọc lặp lại; cách xử lý phantom và các loại read phụ thuộc database và cơ chế MVCC hoặc locking.

SERIALIZABLE hướng đến kết quả tương đương một thứ tự thực thi tuần tự. Nó không nhất thiết có nghĩa database chạy từng transaction một. Database có thể dùng khóa hoặc phát hiện xung đột, và ứng dụng có thể phải retry transaction bị hủy.

Trong bài trừ số dư, em bắt đầu từ invariant không âm. Một cập nhật có điều kiện trong transaction, kết hợp unique constraint và ghi ledger nguyên tử, có thể phù hợp mà không cần bật SERIALIZABLE toàn hệ thống. Với quy tắc phức tạp trên nhiều dòng dễ gặp write skew, em cân nhắc khóa rõ ràng hoặc SERIALIZABLE.

Trade-off là giảm concurrency, tăng chờ hoặc số lần retry khi contention cao. Em xác nhận database, loại query, index và cấu hình thực tế. Retry toàn transaction chỉ an toàn nếu không vô tình lặp lại tác động ngoài database như gửi lệnh ngân hàng.
""", [("REPEATABLE_READ có luôn ngăn phantom không?", "Không trả lời bằng một khẳng định áp dụng cho mọi database. Cần phân biệt chuẩn isolation với implementation, consistent read và locking read.")], "Không chọn SERIALIZABLE chỉ vì nghiệp vụ có tiền.", refs=("mysql",))

add("bean-life", "Spring & Database", "Spring bean lifecycle và BeanFactoryPostProcessor", "Bean definition trước • bean instance sau • shutdown có điều kiện", """
Ở mức tổng quan, Spring đọc bean definitions, xử lý metadata, tạo instance, inject dependency và chạy các bước initialization. BeanPostProcessor có thể can thiệp quanh initialization, chẳng hạn để tạo proxy; @PostConstruct là một hook sau khi dependency đã được thiết lập.

BeanFactoryPostProcessor làm việc với metadata của bean definitions trước giai đoạn khởi tạo bean thông thường. Nó khác BeanPostProcessor vốn làm việc với bean instance. Em không dùng BeanFactoryPostProcessor để vội lấy và khởi tạo các bean nghiệp vụ, vì có thể làm lệch lifecycle mong đợi.

Ví dụ, em dùng initialization nhẹ để kiểm tra cấu hình bắt buộc. Em tránh gọi ngân hàng lâu hoặc chạy batch lớn trong @PostConstruct vì có thể khiến ứng dụng không khởi động được và khó vận hành. Công việc dài nên có lifecycle hoặc worker phù hợp, với trạng thái theo dõi được.

Khi context đóng đúng cách, các destruction callbacks như @PreDestroy có thể dọn tài nguyên. Nhưng process bị kill cưỡng bức thì không bảo đảm hook chạy. Vì thế correctness của giao dịch không được phụ thuộc vào việc luôn chạy cleanup; dữ liệu và recovery phải chịu được crash ở bất kỳ thời điểm nào.
""", [("@PostConstruct có chắc mọi bean khác đã sẵn sàng không?", "Không nên suy rộng như vậy. Nó thuộc initialization của bean; cần chọn hook phù hợp nếu công việc đòi toàn bộ ứng dụng đã sẵn sàng.")], "Graceful shutdown hữu ích nhưng không thay thế crash recovery.", priority=False)

add("security-chain", "Spring & Database", "Spring Security xử lý request và SecurityContext thế nào?", "Filter chain → authentication → authorization → cleanup", """
Trong ứng dụng servlet, Spring Security làm việc thông qua một chuỗi filter trước controller. FilterChainProxy chọn SecurityFilterChain phù hợp với request. Các filter thực hiện những nhiệm vụ như xử lý credential, thiết lập thông tin xác thực và kiểm tra quyền theo cấu hình.

Ví dụ, request mang bearer token. Thành phần xác thực kiểm tra token rồi tạo Authentication để lưu trong SecurityContext. Tầng authorization dùng danh tính và authorities đó để quyết định có được gọi chức năng hay không. Em vẫn kiểm tra quyền trên tài nguyên cụ thể, chẳng hạn tài khoản ngân hàng có thuộc người đang gọi không.

SecurityContextHolder thường dùng ThreadLocal trong mô hình servlet, nên em không mặc định context tự đi theo công việc gửi sang executor. Khi cần truyền context, em dùng cơ chế hỗ trợ phù hợp và bảo đảm cleanup. Session-based và stateless token authentication cũng có cách lưu/khôi phục context khác nhau.

OncePerRequestFilter hỗ trợ tránh thực thi trùng trong phạm vi dispatch được thiết kế, nhưng async và error dispatch có tùy chọn riêng. Em không tự viết một bộ xác minh JWT sơ sài nếu framework đã có resource-server support. Lỗi chưa xác thực thường khác với đã xác thực nhưng không đủ quyền.
""", [("Có role USER là xem được mọi giao dịch của user khác không?", "Không. Role chỉ là một phần; cần object-level authorization dựa trên owner/tenant và policy cho từng tài nguyên.")], "Decode token không phải authentication; authentication không thay object-level authorization.", refs=("spring-security",))

add("cache", "Spring & Database", "@Cacheable, Redis TTL, eviction và cache invalidation", "Cache dữ liệu phù hợp • nguồn sự thật rõ • stale và race", """
Cache giúp giảm latency và tải cho nguồn dữ liệu chính. Với cache-aside, ứng dụng kiểm tra cache, nếu miss thì đọc database và ghi vào cache. @Cacheable hỗ trợ bao quanh lời gọi method theo cơ chế Spring cache; @CacheEvict dùng để loại bỏ entry theo chính sách cập nhật.

Em thiết kế key có đủ phạm vi như tenant, đối tượng và phiên bản dữ liệu, rồi xác định TTL theo mức độ chấp nhận stale. TTL là thời hạn entry, còn eviction do giới hạn memory là một lý do khác khiến key bị loại. Không nên giả định key còn TTL thì chắc vẫn tồn tại.

Ví dụ, cấu hình hiển thị hoặc danh sách ngân hàng có thể cache; nhưng em không dùng số dư cache cũ làm căn cứ cuối cùng cho phép rút tiền. Khi ghi database rồi invalidate cache, vẫn có race giữa reader và writer, nên cần đánh giá consistency thực sự, thay vì nghĩ thêm annotation là xong.

Write-through cập nhật qua lớp cache đồng bộ với nơi lưu theo thiết kế; write-behind ghi bền vững sau, có rủi ro mất hoặc đảo thứ tự nếu không kiểm soát. Em dùng TTL jitter, single-flight hoặc refresh có giới hạn để giảm stampede, và thiết kế fallback khi Redis lỗi để không đánh sập database.
""", [("Xóa cache trước hay sau commit?", "Thường cần gắn với commit thành công, nhưng thứ tự đó không tự loại mọi race. Em phân tích phiên bản dữ liệu và cơ chế invalidation nếu cần bảo đảm mạnh hơn.")], "Cache Redis không phải nguồn sự thật mặc định cho tiền.")

add("rest", "Spring & Database", "REST versioning, error handling và HATEOAS", "Hợp đồng ổn định → lỗi có ý nghĩa → tra cứu kết quả", """
Em thiết kế API từ tài nguyên và hành vi nghiệp vụ, với request validation, quyền truy cập và mã lỗi ổn định. Với giao dịch bất đồng bộ, response nên trả transaction ID cùng trạng thái; client có API tra cứu thay vì đoán kết quả từ việc request có timeout hay không.

Em phân biệt HTTP status với business error code. @ControllerAdvice có thể chuẩn hóa lỗi, gồm code, thông điệp phù hợp và correlation ID, nhưng không trả stack trace, token hoặc dữ liệu nhạy cảm cho client. Lỗi bị từ chối chắc chắn cần khác với kết quả đang xác minh để client không retry sai.

Về versioning, em ưu tiên thay đổi tương thích như thêm field tùy chọn khi hợp đồng cho phép. Nếu thay đổi ngữ nghĩa hoặc cấu trúc phá vỡ client, em có kế hoạch phiên bản mới và thời gian chuyển đổi, chẳng hạn qua URL version hoặc header theo quy ước thống nhất.

HATEOAS bổ sung các liên kết hoặc hành động có thể thực hiện từ trạng thái tài nguyên. Ví dụ, giao dịch pending có link tra cứu. Nó có thể giúp client khám phá luồng, nhưng tăng chi phí hợp đồng và không bắt buộc cho mọi API. Em ưu tiên trạng thái chính xác, idempotency và tài liệu rõ trước.
""", [("Frontend timeout nên báo gì?", "Nếu server có thể đã nhận giao dịch, UI báo đang xác minh và dùng transaction ID/idempotency key để truy vấn hoặc retry đúng hợp đồng, không tạo một ý định thanh toán mới.")], "HTTP 200 không tự chứng minh nghiệp vụ tiền đã hoàn tất.", priority=False)

add("idempotency", "Giao dịch & Distributed", "Thiết kế idempotency key cho payment API", "Scope + payload fingerprint + unique constraint + trạng thái bền vững", """
Idempotency nghĩa là lặp lại cùng một yêu cầu không tạo thêm tác động nghiệp vụ ngoài lần xử lý đầu. Em xác định key theo một ý định giao dịch và scope rõ ràng, chẳng hạn user hoặc merchant cộng loại thao tác. Client giữ nguyên key khi retry vì chưa biết kết quả.

Server lưu key, fingerprint của request đã chuẩn hóa và transaction ID. Unique constraint tại database giúp xử lý hai request đồng thời. Cùng key và cùng payload thì trả giao dịch hoặc kết quả hiện có; cùng key nhưng khác số tiền hay tài khoản đích thì từ chối do xung đột hợp đồng.

Em ghi nhận yêu cầu và cập nhật nghiệp vụ liên quan trong cùng transaction hoặc một giao thức bền vững rõ ràng. Nếu chỉ check Redis rồi tạo giao dịch, crash hoặc race ở giữa có thể tạo lỗ hổng. Cache có thể tăng tốc tra cứu nhưng không thay thế lớp bảo vệ bền vững.

Khi request đầu vẫn xử lý, request sau nhận cùng transaction ID và trạng thái phù hợp. Retention của key phải bao phủ cửa sổ retry/replay và quy định nghiệp vụ. Trade-off là tốn storage và phải xử lý trạng thái dang dở; không nên xóa key ngay khi hoàn tất rồi vô tình cho retry muộn chạy lại.
""", [("Có key ở API là đủ chống trùng toàn hệ thống chưa?", "Chưa. Worker, callback, ledger posting và lệnh ngân hàng cần định danh và cơ chế chống tác động trùng tương ứng.")], "Idempotency key phải giữ nguyên cho retry cùng ý định, không sinh mới mỗi lần bấm lại.")

add("balance", "Giao dịch & Distributed", "Hai request cùng rút tiền: bảo vệ số dư thế nào?", "Check và update nguyên tử • hold • ledger cùng transaction", """
Em không đọc số dư về Java rồi kiểm tra và ghi lại một cách rời rạc, vì hai request có thể cùng thấy số dư cũ. Em cần bảo vệ invariant ngay tại nơi dữ liệu được quản lý.

Một cách là cập nhật có điều kiện trong database: giảm available và tăng held chỉ khi available còn đủ. Em kiểm tra số dòng được cập nhật và đặt việc giữ tiền, tạo transfer và ghi nhận sự kiện cần phát trong cùng local transaction. Nếu một bước thất bại, các thay đổi nội bộ rollback cùng nhau.

Một lựa chọn khác là SELECT FOR UPDATE rồi kiểm tra và cập nhật trong transaction ngắn. Optimistic locking dùng version phù hợp khi contention thấp hơn, nhưng xung đột cao có thể làm retry nhiều. Em chọn dựa trên workload, database và yêu cầu nghiệp vụ chứ không mặc định một cách luôn tốt nhất.

Sau khi đã giữ tiền, gọi ngân hàng ở ngoài transaction dài. Thành công thì chốt hold theo mô hình ledger; thất bại chắc chắn thì release một lần. Kết quả chưa rõ không tự release. Em thêm unique constraint theo tác động nghiệp vụ để callback trùng không chốt hoặc trả tiền hai lần.
""", [("Redis distributed lock có đủ không?", "Không nên là lớp bảo vệ duy nhất: lease có thể hết hạn khi worker còn chạy. Invariant vẫn cần constraint/transaction hoặc fencing phù hợp ở tài nguyên được bảo vệ.")], "Khóa JVM không bảo vệ nhiều pod; lock có TTL không làm mọi thao tác phía sau tự an toàn.")

add("outbox", "Giao dịch & Distributed", "Database commit nhưng publish event thất bại thì sao?", "Outbox nguyên tử → relay có retry → consumer dedupe", """
Đây là vấn đề dual write: database và broker là hai hệ thống khác nhau. Nếu em commit nghiệp vụ rồi publish, process có thể chết ở giữa; nếu publish trước rồi database rollback, consumer có thể thấy một sự kiện không tương ứng dữ liệu đã commit.

Transactional outbox ghi thay đổi nghiệp vụ và bản ghi event trong cùng database transaction. Relay hoặc CDC đưa event từ outbox sang broker. Nếu publish lỗi thì có thể gửi lại vì ý định phát event vẫn còn bền vững trong database.

Nhưng relay có thể publish thành công rồi chết trước khi đánh dấu đã gửi, nên duplicate vẫn xảy ra. Consumer cần event ID hoặc định danh tác động nghiệp vụ, và nếu cùng database thì ghi nhận đã xử lý nguyên tử với cập nhật nghiệp vụ. Nếu tác động là gọi ngân hàng, còn cần idempotency hoặc inquiry theo hợp đồng của ngân hàng.

Em theo dõi tuổi event chưa phát, backlog, số lần lỗi và có quy trình replay. Trade-off là thêm relay, storage và vận hành. Outbox giải quyết không bỏ sót ý định đã commit trong giả định lưu trữ phù hợp; nó không tự biến toàn bộ hệ thống thành exactly-once.
""", [("Consumer ghi DB xong nhưng chưa ack thì chết?", "Message có thể được giao lại; bản ghi dedupe và hiệu ứng nghiệp vụ phải được commit cùng nhau để lần sau không áp dụng lần hai.")], "Không đánh dấu đã gửi trước khi publish rồi chấp nhận mất event.")

add("messaging", "Giao dịch & Distributed", "Kafka, RabbitMQ, ordering và exactly-once", "Phạm vi bảo đảm → key → replay → external side effects", """
Em chọn broker theo nhu cầu thay vì theo tên công nghệ. Kafka phù hợp với log sự kiện có retention và replay, consumer group và partition để scale. RabbitMQ thường thuận tiện cho routing và work queue với acknowledgment; bảo đảm cụ thể vẫn phụ thuộc cấu hình và loại queue.

Pub/sub giúp nhiều nhóm xử lý cùng sự kiện, còn competing consumers chia việc trong một nhóm. Với Kafka, ordering nằm trong partition, không phải toàn topic. Nếu cần tuần tự theo tài khoản, em cân nhắc account ID làm key, đồng thời kiểm soát concurrency trong consumer để không tự phá thứ tự xử lý.

At-least-once có thể giao lại message khi lỗi, nên consumer cần idempotent. Các cơ chế exactly-once của Kafka có phạm vi nhất định; cập nhật database bên ngoài hoặc gọi API ngân hàng không tự được bao phủ. Em luôn hỏi exactly once đối với delivery, processing hay business effect.

DLQ lưu những message không xử lý được sau chính sách phù hợp, nhưng phải có người hoặc công cụ xử lý. Replay cần giữ event ID, xét thứ tự và phiên bản schema. Trade-off của ordering chặt là giảm khả năng song song và có thể tạo hot partition.
""", [("Có thể tăng consumer vô hạn để tăng throughput không?", "Không. Trong một consumer group Kafka, số partition giới hạn số consumer chủ động nhận partition; downstream và ordering cũng giới hạn năng lực.")], "Notification failure không được kích hoạt lại giao dịch tiền đã thành công.", refs=("kafka",))

add("saga-ledger", "Giao dịch & Distributed", "Saga, double-entry ledger và event sourcing", "Compensation ≠ rollback • ledger ≠ mặc định event sourcing", """
Saga chia một nghiệp vụ qua nhiều bước local transaction và có hành động bù khi một bước không thể hoàn tất. Compensation là một nghiệp vụ mới để bù tác động, không phải quay ngược thời gian như database rollback. Nó cũng có thể thất bại và cần retry hoặc xử lý ngoại lệ.

Ví dụ, chuyển tiền ra ngân hàng đã thành công thì không thể chỉ rollback database ví để coi như chưa xảy ra. Có thể phải tạo một nghiệp vụ hoàn tiền riêng nếu đối tác và quy định cho phép. Vì vậy state machine cần phân biệt thất bại chắc chắn với chưa biết kết quả.

Double-entry ledger ghi bút toán cân bằng giữa các tài khoản theo từng currency. Em giữ audit trail và sửa sai bằng bút toán đảo hoặc điều chỉnh có tham chiếu, không sửa xóa lịch sử tùy tiện. Available balance và held amount là mô hình phục vụ quyết định chi tiêu, phải được cập nhật nhất quán với nguồn sự thật đã chọn.

Event sourcing lấy chuỗi event làm nguồn để dựng trạng thái, nhưng có ledger không đồng nghĩa mọi service phải event-source. Event sourcing thêm replay, versioning và projection consistency. Em chỉ chọn khi lợi ích truy vết và tái dựng xứng đáng với độ phức tạp, không coi đó là điều kiện bắt buộc để xây ví.
""", [("Ledger có nên sửa dòng cũ để khớp ngân hàng không?", "Không sửa tùy tiện để che sai lệch. Giữ bằng chứng, đối soát nguyên nhân và tạo adjustment có phê duyệt cùng liên kết tới bút toán gốc.")], "Saga không bảo đảm compensation luôn thành công ngay lập tức.")

add("resilience", "Giao dịch & Distributed", "Timeout, retry, circuit breaker và bulkhead", "Giới hạn chờ • retry an toàn • cô lập lỗi • không bão retry", """
Timeout giới hạn thời gian chờ. Retry thử lại một lỗi có khả năng tạm thời. Circuit breaker tạm ngăn gọi downstream khi dấu hiệu lỗi vượt ngưỡng, rồi cho một số lời gọi thăm dò khi half-open. Bulkhead tách tài nguyên để lỗi của một nhóm không chiếm hết năng lực của nhóm khác.

Với ngân hàng, em đặt deadline tổng và timeout từng lần gọi, retry có giới hạn với exponential backoff và jitter. Em chỉ retry lệnh có cơ chế an toàn theo hợp đồng, và không retry lỗi nghiệp vụ như tài khoản không hợp lệ theo cùng cách lỗi mạng.

Em tránh nhiều tầng cùng retry vì số lần gọi có thể nhân lên. Với Resilience4j, em xác định thứ tự kết hợp decorator, loại lỗi được tính vào breaker và giới hạn concurrency. Breaker mở không có nghĩa giao dịch trước đó chắc chắn thất bại; kết quả chưa rõ vẫn phải được inquiry hoặc đối soát.

Trade-off là fail-fast có thể từ chối một số request khi downstream đang hồi phục, còn queue quá lớn làm latency tăng. Em theo dõi error rate, slow-call rate, pending age và tách pool theo ngân hàng. Fallback cho giao dịch tiền không được trả thành công giả hoặc tự hoàn tiền khi chưa có căn cứ.
""", [("Breaker có thay timeout không?", "Không. Breaker đánh giá tình trạng theo thống kê; một lời gọi được phép đi qua vẫn cần deadline và timeout riêng.")], "Một status timeout không phải kết luận nghiệp vụ thất bại.")

add("cap-scale", "Giao dịch & Distributed", "CAP, scaling, index và sharding trong payment", "Theo từng thao tác • đo trước • shard sau", """
CAP nói về đánh đổi consistency và availability khi có network partition trong mô hình phân tán. Em không gắn nhãn CP hay AP cho toàn bộ payment system. Khi không xác minh được quyền ghi số dư nhất quán, em có thể dừng hoặc giữ pending thao tác chi tiền; lịch sử hoặc thông báo có thể chấp nhận dữ liệu chậm hơn.

Consistency trong CAP cũng không đồng nghĩa mọi nghĩa của chữ consistency trong ACID. Em cần nói rõ bảo đảm mà thao tác yêu cầu. Giảm khả năng ghi khi partition là một quyết định bảo vệ invariant, không có nghĩa hệ thống phải ngừng tất cả API đọc.

Về scale, em đo bottleneck trước: query plan, index, lock, connection pool, CPU, queue và downstream. Scale up đơn giản nhưng có giới hạn; scale out app stateless giúp phân tải nhưng không tự scale database hay ngân hàng. Đọc lịch sử có thể dùng index phù hợp và cursor pagination trước khi nghĩ đến sharding.

Hash sharding thường phân bố tải nhưng khó range query và reshard; range sharding thuận truy vấn theo khoảng nhưng có thể tạo hotspot. Shard theo account làm giao dịch giữa hai account khó hơn. Em chọn khi số liệu chứng minh nhu cầu, với routing, migration và recovery rõ ràng.
""", [("100K concurrent users có phải 100K TPS không?", "Không. Cần tỷ lệ user đang thao tác, số request trên mỗi người mỗi giây và read/write mix; số kết nối đồng thời không đồng nhất số giao dịch mỗi giây.")], "Không viện CAP để chấp nhận chi vượt số dư.")
add("oauth", "Bảo mật & Identity", "OAuth2, OpenID Connect và JWT khác nhau thế nào?", "Ủy quyền • danh tính • định dạng token", """
OAuth2 là framework ủy quyền: một client được cấp quyền truy cập tài nguyên trong phạm vi cho phép. OpenID Connect xây thêm lớp danh tính trên OAuth2, phục vụ việc xác thực người dùng. JWT là định dạng token, nên không cùng cấp khái niệm với OAuth2.

Em phân biệt authentication là xác định chủ thể, còn authorization là quyết định chủ thể được làm gì. Trong tích hợp liên quan tài khoản ngân hàng, có token hợp lệ chưa đủ; còn phải kiểm tra scope, audience và quyền với tài khoản cụ thể.

Với Authorization Code cùng PKCE, client tạo verifier và challenge, đưa challenge vào bước xin authorization. Sau khi nhận code, client đổi code cùng verifier tại token endpoint. Authorization server kiểm tra quan hệ giữa chúng để giảm nguy cơ sử dụng code bị đánh cắp. Em xác minh redirect URI, liên kết response với phiên bắt đầu flow và dùng state/nonce đúng mục đích của giao thức.

Client Credentials phù hợp cho một số giao tiếp service-to-service, đại diện quyền của client. Nó không tự thay thế consent của người dùng. Em không tự xây cơ chế OAuth từ đầu nếu có giải pháp tiêu chuẩn phù hợp; triển khai sai callback hoặc token validation có thể phá vỡ bảo mật dù tên flow đúng.
""", [("ID token có dùng thay access token gọi mọi API không?", "Không. ID token cung cấp thông tin xác thực cho client theo audience của nó; API cần loại token và audience được thiết kế cho resource server đó.")], "OAuth2 không phải định dạng token; JWT không mặc định là token đăng nhập.", refs=("oauth", "oidc"))

add("jwt", "Bảo mật & Identity", "Access token, refresh token và kiểm tra JWT", "Verify, không chỉ decode • vòng đời • revocation", """
Access token dùng để truy cập tài nguyên trong phạm vi và thời gian được cấp. Refresh token được dùng với authorization server để xin access token mới; nó không nên được gửi như credential đến các resource API thông thường.

JWT thường được ký, không mặc định được mã hóa. Payload có thể đọc được, nên không đưa secret vào rồi nghĩ chữ ký sẽ che giấu nó. Khi nhận token, em dùng thư viện tin cậy để kiểm tra signature với khóa đáng tin, allowlist thuật toán, issuer, audience và thời hạn cùng các claim liên quan.

Em quản lý token theo môi trường client. Backend cần bảo vệ secret và hạn chế quyền; ứng dụng browser cần cân nhắc XSS, CSRF và mô hình BFF/cookie phù hợp. Nếu dùng cookie, HttpOnly, Secure và SameSite là các lớp bảo vệ có vai trò riêng, không phải giải pháp xóa hết mọi rủi ro.

JWT tự chứa claim làm validation cục bộ thuận tiện nhưng thu hồi tức thời khó hơn. Em có thể kết hợp access token ngắn hạn, refresh token rotation và cơ chế revocation theo yêu cầu. Logout không tự khiến mọi access token đã phát hành biến mất, nên thiết kế session phải nói rõ thời gian và phạm vi thu hồi.
""", [("Token bị lộ thì đổi chữ ký có giải quyết ngay không?", "Cần quy trình ứng phó gồm thu hồi, rotation và giới hạn tác động. Đổi key có thể ảnh hưởng nhiều token và các cache verifier; không phải nút bấm đơn giản cho mọi trường hợp.")], "Không log bearer token hoặc refresh token.", refs=("jwt", "oauth"))

add("sso", "Bảo mật & Identity", "SSO: SAML, OIDC và session qua nhiều ứng dụng", "IdP session ≠ app session ≠ access token", """
SSO cho phép người dùng tận dụng phiên đăng nhập tại identity provider để truy cập nhiều ứng dụng mà không phải nhập credential lặp lại trong điều kiện phù hợp. SAML thường dùng assertion XML trong federated identity, còn OpenID Connect cung cấp lớp xác thực dựa trên OAuth2 và token/claim theo giao thức của nó.

Em lựa chọn theo hệ sinh thái và khả năng của identity provider, không chỉ theo tiêu chí mới hay cũ. Một tổ chức dùng SAML ổn định có thể tiếp tục tích hợp SAML; ứng dụng web hoặc mobile dùng OIDC cần triển khai flow và validation đúng.

Em phân biệt phiên ở IdP với session của từng ứng dụng. Sau SSO, mỗi ứng dụng có thể tạo session riêng; các backend service dùng access token phù hợp khi gọi API. Không cần và không nên mặc định tất cả service đọc cùng một session object hay chia sẻ cookie tùy tiện giữa các domain.

Khi logout, phải xác định chỉ logout ứng dụng hiện tại hay toàn bộ hệ sinh thái, và cơ chế front-channel/back-channel hoặc thu hồi nào được hỗ trợ. Trade-off của token tự xác minh là giảm phụ thuộc trực tiếp nhưng khó thu hồi ngay; session store tập trung giúp kiểm soát nhưng thêm phụ thuộc vận hành.
""", [("IdP down thì user đang đăng nhập có dùng tiếp không?", "Tùy thời hạn token, phiên ứng dụng và cách validation. Không suy ra tự động là tất cả phải logout hoặc tất cả vẫn hoạt động vô hạn.")], "SSO không đồng nghĩa một session dùng chung cho mọi microservice.", priority=False, refs=("oidc", "saml"))

add("crypto", "Bảo mật & Identity", "Hash, encryption, HMAC và digital signature", "Bí mật • toàn vẹn • nguồn gửi • khóa nào làm gì", """
Encryption bảo vệ tính bí mật: bên có khóa phù hợp có thể giải mã nội dung. Hash tạo giá trị tóm tắt và không được thiết kế để giải mã ngược, nhưng hash thuần không chứng minh ai gửi vì người sửa dữ liệu cũng có thể tính hash mới.

HMAC dùng shared secret để kiểm tra tính toàn vẹn và xác thực trong phạm vi các bên biết secret. Digital signature dùng private key để ký và public key để kiểm tra. Bên verify không cần giữ private key, nhưng phải tin đúng public key và quản lý chứng thư hoặc phân phối khóa đúng.

Ví dụ, callback ngân hàng có chữ ký trên payload. Em kiểm tra đúng tập trường và cách canonicalization theo hợp đồng, vì chỉ đổi cách biểu diễn JSON cũng có thể làm khác byte được ký. Chữ ký hợp lệ chưa ngăn được một thông điệp cũ bị gửi lại, nên còn cần freshness và chống tác động trùng.

Em dùng thư viện và thuật toán tiêu chuẩn, không tự chế crypto. Password cần cơ chế password hashing có salt và work factor phù hợp, không lưu bằng hash nhanh đơn thuần. Trade-off quan trọng nằm ở quản lý khóa, rotation, quyền truy cập và khả năng điều tra khi khóa bị lộ, không chỉ tên thuật toán.
""", [("HMAC có chứng minh bên nào trong hai bên shared secret đã ký không?", "Không phân biệt được một cách mật mã nếu cả hai đều biết cùng secret. Đó là khác biệt quan trọng với mô hình chữ ký bất đối xứng.")], "Chữ ký số không che giấu nội dung; hash không phải mã hóa.")

add("tls-storage", "Bảo mật & Identity", "AES-256 at rest, TLS in transit và mTLS", "Thuật toán + mode + key management + trust boundary", """
Mã hóa at rest bảo vệ dữ liệu lưu trữ, ví dụ database, object storage hoặc backup. Mã hóa in transit bảo vệ dữ liệu trên đường truyền. Hai lớp này bổ sung nhau; có HTTPS không bảo vệ một bản backup bị lộ, còn mã hóa ổ đĩa không ngăn app có quyền đọc rồi log dữ liệu ra ngoài.

Với AES-256, em không chỉ nhìn độ dài khóa. Cần mode phù hợp như authenticated encryption, quản lý nonce đúng yêu cầu, bảo vệ khóa bằng KMS hoặc HSM khi phù hợp và kiểm soát quyền giải mã. Envelope encryption tách data key với key bảo vệ nó, giúp vận hành và rotation linh hoạt hơn.

TLS 1.2 hoặc 1.3 cần cấu hình phù hợp, kiểm tra certificate, hostname và trust chain. Không tắt certificate validation chỉ để tích hợp chạy được. mTLS bổ sung xác thực client bằng certificate, trong khi TLS server-auth thông thường chủ yếu xác thực server với client.

Khi TLS kết thúc ở gateway, em kiểm tra cả đường truyền nội bộ sau đó. Trade-off là quản lý certificate, rotation và compatibility. Payload signing vẫn có thể cần để kiểm tra thông điệp ở tầng ứng dụng qua các trung gian; em xác định threat model thay vì coi một lớp mã hóa bảo vệ tất cả.
""", [("Database encrypted rồi thì SQL injection có đọc được dữ liệu không?", "Có thể, nếu truy vấn đi qua ứng dụng hoặc database có quyền giải mã. At-rest encryption không thay input handling, authorization và giới hạn quyền.")], "Không lưu key cạnh ciphertext rồi coi như đã giải quyết quản lý khóa.", refs=("tls",))

add("pci", "Bảo mật & Identity", "PCI DSS, tokenization và audit logging", "Giảm dữ liệu nhạy cảm • phân loại đúng • audit không lộ secret", """
Em hiểu PCI DSS là tiêu chuẩn bảo vệ dữ liệu tài khoản thẻ trong phạm vi áp dụng, không phải một thư viện hay một lần chạy scanner là hoàn tất. Trong thiết kế, em ưu tiên giảm dữ liệu thẻ mà hệ thống phải tiếp xúc và lưu trữ, dùng nhà cung cấp phù hợp và xác định scope với đội bảo mật.

Tokenization thay dữ liệu nhạy cảm bằng token; khả năng ánh xạ hoặc phục hồi do hệ thống tokenization quản lý. Nó khác encryption là biến đổi dữ liệu bằng khóa để giải mã. Tokenization có thể giúp giảm exposure, nhưng không tự loại mọi hệ thống ra khỏi scope, nhất là nơi có thể detokenize.

PAN không phải luôn bị cấm lưu, nhưng nếu cần lưu thì phải đáp ứng yêu cầu bảo vệ và retention phù hợp. Với hệ thống merchant thông thường, sensitive authentication data như CVV, full track hoặc PIN block không được giữ sau authorization, kể cả mã hóa; các ngoại lệ chuyên biệt cho issuing cần đánh giá riêng.

Audit log ghi ai làm gì, khi nào, với tài nguyên nào và kết quả ra sao; phải hạn chế sửa, kiểm soát truy cập và theo dõi. Em không log token, CVV hay raw payload nhạy cảm. Log giúp điều tra nhưng không thay ledger hoặc đối soát; retention và masking phải theo policy và phạm vi thực tế.
""", [("Mask PAN trên UI có đủ bảo vệ database không?", "Không. Masking hiển thị và bảo vệ dữ liệu lưu trữ là hai vấn đề khác nhau; backup, log và export cũng phải được xét.")], "Tránh câu tuyệt đối 'PCI cấm lưu mọi dữ liệu thẻ'; phân biệt PAN với SAD.", priority=False, refs=("pci-sad", "pci-pan"))

add("rate-limit", "Giao dịch & Distributed", "Token Bucket, Leaky Bucket và Redis rate limiter", "Burst budget • tốc độ xử lý • atomic update • lỗi Redis", """
Rate limiter kiểm soát số yêu cầu theo thời gian để bảo vệ tài nguyên và thực thi quota. Token Bucket có sức chứa và tốc độ bổ sung token; request tiêu thụ token nên có thể cho phép burst trong giới hạn. Leaky Bucket ở dạng shaping queue đưa công việc ra với tốc độ đều và queue hữu hạn; cũng có biến thể dùng để meter/reject mà không thực sự giữ request.

Với API payment, em xác định giới hạn theo user, merchant, IP và ngân hàng ở các tầng phù hợp. IP không đủ đại diện người dùng vì có NAT và proxy. Tác động trừ tiền vẫn cần idempotency riêng; rate limit không phải chống duplicate về nghiệp vụ.

Trong Redis, em dùng thao tác nguyên tử như Lua script để đọc thời điểm, refill token, quyết định và cập nhật trong một lượt, thay vì GET rồi SET rời rạc. Em xác định nguồn thời gian, TTL an toàn và key scope. Với cluster, thao tác nhiều key phải xét hash slot và tránh hot key.

Khi hết quota, API trả lỗi và hướng dẫn retry phù hợp. Redis lỗi thì fail-open hay fail-closed tùy rủi ro: thao tác nhạy cảm có thể chặn hoặc dùng giới hạn dự phòng chặt, còn API đọc có thể cho qua có kiểm soát. Em thừa nhận giới hạn consistency khi failover và không dùng limiter làm invariant số dư.
""", [("Rate limit khác concurrency limit không?", "Rate limit giới hạn theo thời gian; concurrency limit giới hạn số công việc đang xử lý. Ngân hàng chậm có thể làm concurrency tăng dù tốc độ request không đổi.")], "TTL key không được làm reset quota sớm và cho burst ngoài thiết kế.", refs=("redis",))

add("testing", "Vận hành & Chất lượng", "Test hệ thống giao dịch tiền như thế nào?", "Invariant → failure injection → duplicate/concurrency → recovery", """
Em bắt đầu từ invariant và các ranh giới lỗi, không chỉ test endpoint trả 200. Unit test kiểm tra quy tắc nghiệp vụ, state transition và mapping. Integration test kiểm tra transaction, constraint và broker/database behavior; contract test bảo vệ giả định với ngân hàng.

Những tình huống quan trọng là hai request đồng thời cùng idempotency key, hai yêu cầu rút khác nhau tranh số dư, ngân hàng đã xử lý nhưng response mất, callback trùng hoặc đến trước response, và consumer chết sau DB commit nhưng trước ack.

Em dùng stub hoặc simulator có thể chủ động tạo timeout, response muộn và lỗi có kiểm soát. Với concurrency, em thiết lập điểm đồng bộ và kiểm tra trạng thái cuối cùng thay vì chỉ chạy hai thread rồi hy vọng race xảy ra. Sau retry và replay, tổng tác động tiền phải vẫn đúng và lịch sử phải truy vết được.

Em bổ sung load test theo read/write mix và downstream latency thực tế, đồng thời kiểm tra deployment và recovery. Trade-off là không thể mô phỏng hoàn hảo ngân hàng production; cần sandbox, contract version và giám sát. Coverage phần trăm cao không chứng minh đã test đúng failure mode quan trọng.
""", [("Test lỗi timeout cần assert gì?", "Không chỉ exception; cần assert trạng thái chưa rõ, hold không được release tùy tiện, retry giữ đúng định danh và callback muộn chỉ chốt một lần.")], "Không dùng ngân hàng thật để thử giao dịch có tác động tiền khi chưa có môi trường và quyền phù hợp.")

add("deployment", "Vận hành & Chất lượng", "Docker, Kubernetes, CI/CD và graceful shutdown", "Reproducible build • readiness • drain • compatible migration", """
Docker giúp đóng gói ứng dụng với runtime và dependency; Kubernetes quản lý chạy, phân tải và phục hồi workload theo cấu hình. Chúng không tự làm nghiệp vụ chịu lỗi đúng, nên em vẫn thiết kế restart ở bất kỳ điểm nào không gây mất hoặc nhân đôi tác động tiền.

Readiness quyết định pod đã sẵn sàng nhận traffic chưa; liveness hỗ trợ phát hiện process cần khởi động lại. Nếu gắn liveness với một ngân hàng đang down, có thể gây restart hàng loạt không cần thiết. Em đặt request/limit tài nguyên dựa trên đo đạc và xem tác động CPU throttling, memory limit lên JVM.

Khi shutdown, em ngừng nhận công việc mới, drain request hoặc dừng lấy message, cho công việc hiện tại thời gian hợp lý rồi đóng tài nguyên. Tuy nhiên kill cưỡng bức vẫn có thể xảy ra; message ack và transaction phải cho phép phục hồi an toàn.

Pipeline build, kiểm thử, kiểm tra dependency và phát hành artifact nhất quán. Database migration cần tương thích khi phiên bản cũ và mới cùng chạy, thường theo expand rồi contract. Rollback application không tự rollback schema hoặc dữ liệu đã biến đổi. Em theo dõi metric nghiệp vụ sau canary, không chỉ pod Running.
""", [("Scale thêm pod có giải quyết connection pool cạn không?", "Có thể làm tổng số connection tăng vượt sức database. Cần budget toàn hệ thống, timeout, giới hạn concurrency và kiểm tra query trước.")], "Không dùng readiness/liveness như một loại health check duy nhất cho mọi phụ thuộc.")

add("ai-frontend", "Vận hành & Chất lượng", "Frontend payment và sử dụng AI-assisted tools", "UX thể hiện đúng trạng thái • AI có kiểm chứng", """
Ở frontend giao dịch, em ưu tiên phản ánh đúng trạng thái server. Nút bị disable giúp giảm thao tác lặp nhưng không thay idempotency backend. Khi mạng lỗi, UI không tự kết luận thất bại; nó giữ transaction ID hoặc định danh yêu cầu để tra cứu và cho người dùng thông tin rõ ràng.

Nếu dùng React, em tách trạng thái nhập liệu với trạng thái giao dịch, xử lý request cũ trả về muộn và cleanup polling khi component không còn cần. Dữ liệu số tiền được validate theo hợp đồng, còn backend vẫn kiểm tra lại quyền, amount và hạn mức.

Về AI, em có thể dùng để đề xuất test case, giải thích code, soạn tài liệu hoặc tạo bản nháp implementation. Nhưng em chịu trách nhiệm kiểm tra diff, security assumptions và chạy test phù hợp. Với logic tiền và concurrency, em đặc biệt kiểm chứng các tình huống lỗi thay vì chỉ thấy code compile.

Em tuân thủ policy về dữ liệu đưa vào công cụ, tránh gửi secret và dữ liệu khách hàng. Khi kể kinh nghiệm, em chỉ nêu hiệu quả thực sự đã đo hoặc quan sát, không tự bịa tỷ lệ tăng năng suất. Trade-off là AI có thể tạo code nhìn hợp lý nhưng sai phiên bản hoặc sai ranh giới transaction.
""", [("AI đưa ra code idempotency dùng cache, em review gì?", "Em kiểm tra atomicity, durability, multi-instance, payload mismatch, retention, crash window và recovery, thay vì chỉ kiểm tra API cache được gọi đúng.")], "Không nhận công lao hoặc số liệu hiệu quả chưa từng có.", priority=False)
add("exp-intro", "Kinh nghiệm thực tế", "Giới thiệu bản thân và lý do chọn Bank Solutions", "90 giây mở đầu + 2 phút dự án + 1 phút liên hệ vị trí", """
Em có [số năm thật] kinh nghiệm phát triển phần mềm, chủ yếu với [stack thực tế]. Trong công việc gần đây, em tham gia [bài toán sản phẩm] cho [đối tượng sử dụng]. Phần em trực tiếp chịu trách nhiệm là [module/phạm vi], từ [các bước thật sự làm] đến kiểm tra kết quả sau triển khai.

Em xin lấy một phần việc để nói rõ hơn. Khi [bối cảnh hoặc yêu cầu], hệ thống gặp [vấn đề cụ thể]. Mục tiêu của team là [mục tiêu]. Em phụ trách [trách nhiệm cá nhân], phối hợp với [vai trò liên quan]. Em phân biệt phần mình tự thực hiện với các quyết định do cả team cùng đưa ra.

Ban đầu có hai hướng là [phương án A] và [phương án B]. Em đã kiểm tra [bằng chứng hoặc thử nghiệm]. Cuối cùng, [em/team] chọn [phương án] vì [ràng buộc quan trọng nhất]. Điểm đánh đổi là [hạn chế], nên em bổ sung [biện pháp kiểm soát]. Phần này giúp em hiểu rõ hơn về [năng lực liên quan vị trí].

Sau khi triển khai, kết quả em quan sát được là [số liệu đã xác minh hoặc bằng chứng định tính]. Nếu không có metric lịch sử đáng tin, em sẽ nói rõ chưa thể khẳng định một tỷ lệ cải thiện. Điều em chắc chắn đã kiểm chứng là [test, phản hồi hoặc log có thật].

Qua phần việc đó, em học được [bài học cụ thể]. Nếu làm lại, em sẽ [thay đổi dựa trên bài học], vì [lý do]. Đây cũng là hướng em muốn phát triển tiếp: hiểu sâu hơn về consistency, vận hành và recovery thay vì chỉ hoàn thành API ở happy path.

Em quan tâm Bank Solutions vì bài toán kết nối ngân hàng đòi hỏi tính đúng đắn, độ tin cậy và bảo mật cao. Kinh nghiệm [điểm mạnh thật] của em có thể hỗ trợ ở [phần công việc]. Với phần domain em chưa làm trực tiếp, em đang ôn [chủ đề] và em sẽ chủ động học từ hợp đồng tích hợp, quy trình đối soát và cách team xử lý incident.
""", [("Em đã làm fintech thật chưa?", "Nếu chưa, nói thẳng: Em chưa trực tiếp làm hệ thống ngân hàng; phần liên quan em đã làm là [sự thật]. Các thiết kế fintech em vừa trình bày là kiến thức em đang luyện, không phải thành tích production.")], "Điền bằng dữ kiện thật trước buổi phỏng vấn; không đọc nguyên dấu ngoặc vuông.", kind="experience", minutes=4,
extra="<h4>Trước khi luyện</h4><ul><li>Điền 1 dự án, 1 phần việc cá nhân, 1 lựa chọn có đánh đổi.</li><li>Mở đầu trong 60–90 giây; chỉ mở rộng tới 3–5 phút khi manager muốn nghe thêm.</li><li>Không cần kể toàn bộ lịch sử công việc.</li></ul>")

add("exp-system", "Kinh nghiệm thực tế", "Mô tả hệ thống hiện tại trong 3–5 phút", "Bài toán → sơ đồ → một request → ownership → điểm nghẽn", """
Em xin trình bày hệ thống theo bài toán, kiến trúc và phần em phụ trách. Hệ thống phục vụ [đối tượng], với nghiệp vụ chính là [nghiệp vụ]. Quy mô em có dữ liệu là [metric và khoảng thời gian đo]. Những số liệu như peak TPS hoặc p99 mà em chưa trực tiếp theo dõi thì em không muốn đoán; em sẽ giải thích cách em có thể kiểm tra.

Trên sơ đồ, client là [loại client], request đi qua [các thành phần có thật] tới [service]. Service xác thực và kiểm tra [quy tắc], sau đó đọc hoặc ghi [database]. Các công việc [nêu việc] được xử lý [đồng bộ hoặc bất đồng bộ]. Em dùng mũi tên khác nhau để phân biệt HTTP với messaging nếu hệ thống thực sự có cả hai.

Em lấy luồng [tên luồng] làm ví dụ. Đầu vào gồm [dữ liệu], hệ thống kiểm tra [điều kiện], rồi cập nhật [bảng hoặc tài nguyên]. Ranh giới transaction nằm tại [vị trí]. Nếu có lời gọi bên ngoài, kết quả được xử lý bằng [cơ chế thật]. Khi một bước lỗi, hệ thống hiện tại [hành vi thật], và hạn chế em nhận thấy là [hạn chế].

Phần em trực tiếp làm là [phạm vi]. Em đã chọn hoặc đề xuất [quyết định], dựa trên [ràng buộc]. Phương án khác là [phương án], nhưng lúc đó chưa chọn vì [lý do]. Các phần [phạm vi ngoài ownership] do team khác quản lý; em hiểu contract tích hợp nhưng không nhận mình thiết kế implementation bên trong.

Về vận hành, team theo dõi [metric/log/alert có thật]. Một lần hệ thống gặp [vấn đề], em dùng [bằng chứng] để xác định [nguyên nhân hoặc bottleneck]. Kết quả của cải tiến là [bằng chứng]. Nếu traffic tăng nhiều lần, giả thuyết đầu tiên của em là [điểm nghẽn], và em sẽ xác nhận bằng load test cùng [metric] trước khi scale.

Điều em muốn cải thiện tiếp là [điểm cụ thể]. Em chưa thay đổi ngay vì [chi phí hoặc ưu tiên]. Bài học của em là kiến trúc cần phù hợp quy mô và khả năng vận hành, và mọi quyết định lớn cần được kiểm chứng bằng một luồng thực tế cùng failure case.
""", [("Vì sao hệ thống không dùng Kafka/microservices?", "Trả lời bằng workload và nhu cầu thật. Một monolith hoặc luồng đồng bộ có thể phù hợp; không cần xin lỗi vì chưa dùng một công nghệ.")], "Không dùng kiến trúc ví dụ trong tài liệu này để nhận là hệ thống mình đã xây.", kind="experience", minutes=5,
extra="<h4>Vẽ trong lúc nói</h4><p>Client → điểm vào → module/service → database; thêm dependency ngoài và đường async nếu có. Khoanh phần Minh sở hữu, đánh dấu transaction và ít nhất một điểm có thể lỗi.</p>")

add("exp-incident", "Kinh nghiệm thực tế", "Kể một incident hoặc lỗi khó từng xử lý", "Ảnh hưởng → giảm tác động → bằng chứng → sửa → ngăn tái diễn", """
Ở dự án [dự án], em gặp sự cố [triệu chứng] vào [bối cảnh]. Sự cố được phát hiện qua [alert, dashboard hoặc phản ánh]. Ảnh hưởng mà team xác nhận được là [phạm vi]; phần chưa rõ lúc đầu là [điều chưa biết]. Vai trò của em là [vai trò], còn [vai trò khác] phụ trách [phần khác].

Việc đầu tiên của em là [biện pháp giảm ảnh hưởng có thật], đồng thời thông báo tình trạng theo quy trình của team. Em ưu tiên giảm tác động và bảo toàn dữ liệu trước khi cố tìm lời giải hoàn hảo. Em tránh thay nhiều cấu hình cùng lúc vì sẽ khó xác định nguyên nhân và tác dụng của thay đổi.

Ban đầu em đặt giả thuyết [A]. Em kiểm tra [log, trace, metric hoặc query] và thấy [bằng chứng]. Dữ liệu này khiến em loại hoặc điều chỉnh giả thuyết đó. Sau đó em đối chiếu [nguồn thứ hai] để xác định [nguyên nhân]. Em phân biệt triệu chứng nhìn thấy với nguyên nhân gốc, chẳng hạn timeout có thể là hậu quả của pool cạn chứ không phải lỗi mạng.

Em thực hiện [cách khắc phục]. Trước khi áp dụng rộng, em kiểm tra [test hoặc phạm vi thử]. Sau thay đổi, [metric hoặc bằng chứng] cho thấy hệ thống hồi phục. Nếu có dữ liệu dang dở, team xử lý bằng [quy trình thật], và em trực tiếp làm [phần việc].

Sau incident, em bổ sung [alert/test/runbook/giới hạn tài nguyên] để phát hiện hoặc ngăn tình huống tương tự. Kết quả theo dõi sau đó là [kết quả thật], trong [khoảng thời gian]. Nếu chưa đủ thời gian quan sát, em sẽ nói mới xác nhận bản sửa bằng test và giám sát ban đầu, chưa khẳng định vấn đề không bao giờ lặp lại.

Bài học lớn nhất của em là [bài học]. Nếu xử lý lại, em sẽ [cải thiện]. Em cũng nhìn nhận phần mình có thể làm tốt hơn là [trách nhiệm cá nhân], thay vì chỉ quy lỗi cho một người hoặc một dependency.
""", [("Em chưa từng on-call thì kể gì?", "Kể một lỗi khó ở staging hoặc production mà mình thật sự tham gia, nói rõ môi trường và vai trò. Không biến việc đọc postmortem thành việc trực tiếp xử lý.")], "Không bịa số lượng khách hàng bị ảnh hưởng hay mức tiết kiệm tiền.", kind="experience", minutes=5)

add("exp-performance", "Kinh nghiệm thực tế", "Kể một lần tối ưu hoặc lựa chọn thiết kế có đánh đổi", "Baseline → giả thuyết → phương án → phép đo → giới hạn", """
Trong [luồng nghiệp vụ], team nhận thấy [vấn đề] khi [điều kiện tải]. Trước khi sửa, em xác định mục tiêu là [SLO hoặc mục tiêu cụ thể] và lấy baseline từ [nguồn đo]. Em phân biệt thời gian trung bình với phân vị và thời gian trong app với thời gian chờ dependency.

Phần em phụ trách là [phạm vi]. Em xem [query plan, trace, profile hoặc metric] và đưa ra giả thuyết [nguyên nhân]. Em kiểm tra bằng [cách kiểm chứng], thay vì mặc định cứ thêm cache hoặc thêm pod là nhanh hơn.

Có hai phương án là [A] và [B]. Phương án A có lợi về [điểm], nhưng tốn [chi phí]. Phương án B có [ưu và nhược]. Em đề xuất [lựa chọn] vì [ràng buộc quan trọng], đồng thời thống nhất cách đo và rollback nếu kết quả không đạt.

Em triển khai [thay đổi thật], kiểm thử correctness trước rồi đo với workload tương đương. Kết quả trước là [baseline thật], sau là [kết quả thật], ở [điều kiện đo]. Nếu chỉ có benchmark nội bộ, em nói rõ đó không phải số liệu production. Em cũng kiểm tra tác động phụ lên CPU, memory, database hoặc độ mới của dữ liệu.

Trade-off mà team chấp nhận là [đánh đổi]. Ví dụ nếu có cache thật, em cần nói được invalidation, TTL và hành vi khi cache lỗi, chứ không chỉ nói latency giảm. Sau release, em theo dõi [metric] và ghi lại [tài liệu hoặc runbook].

Bài học của em là đo đúng điểm nghẽn giúp chọn thay đổi nhỏ nhưng có tác dụng. Nếu traffic tăng tiếp, em sẽ kiểm tra lại giả thuyết cũ vì bottleneck có thể chuyển sang một thành phần khác; em không coi một kết quả benchmark là kết luận vĩnh viễn.
""", [("Không có số liệu trước thay đổi thì sao?", "Nói rõ giới hạn và dùng bằng chứng có thể kiểm chứng như loại bỏ full scan, số query giảm hoặc test hoàn tất trong giới hạn; không tạo phần trăm ước lượng thành thành tích.")], "So sánh trước/sau phải có điều kiện tải và môi trường tương đương.", kind="experience", minutes=4)

add("exp-conflict", "Kinh nghiệm thực tế", "Bất đồng thiết kế, deadline và ownership", "Rủi ro cụ thể → phương án → trao đổi bằng chứng → quyết định", """
Em xin lấy tình huống [tình huống thật]. Khi đó deadline là [bối cảnh], còn điểm bất đồng là [vấn đề kỹ thuật hoặc phạm vi]. Trách nhiệm của em là [phạm vi], và người có quyền quyết định cuối cùng là [vai trò].

Em bắt đầu bằng việc hiểu mục tiêu của phía còn lại, chẳng hạn thời gian ra mắt, chi phí vận hành hoặc tính đơn giản. Sau đó em trình bày rủi ro theo một tình huống cụ thể: nếu [điều kiện], hệ thống sẽ [hậu quả]. Em cố tránh lập luận chỉ dựa trên sở thích công nghệ.

Em đưa ra [hai hoặc ba lựa chọn có thật], gồm chi phí thực hiện và mức rủi ro còn lại. Nếu có thể, em tạo một thử nghiệm nhỏ hoặc thu thập log để làm rõ điều đang tranh luận. Với rủi ro sai dữ liệu tiền, cách giảm scope hoặc tạm tắt một nhánh chức năng thường đáng cân nhắc hơn bỏ qua lớp bảo vệ.

Cuối cùng, team chọn [quyết định]. Em [đồng ý sau bằng chứng hoặc ghi lại lo ngại và thực hiện quyết định trong phạm vi phù hợp]. Phần em triển khai là [việc], cùng điều kiện theo dõi [metric hoặc tiêu chí]. Kết quả thực tế là [kết quả], và điểm còn chưa tốt là [hạn chế].

Sau đó, em cùng team [việc cải thiện], chẳng hạn ghi ADR, thêm tiêu chí kiểm thử hoặc làm rõ ownership. Bài học của em là bất đồng nên được đưa về mục tiêu, dữ liệu và trách nhiệm, không biến thành cuộc tranh luận ai giỏi hơn.

Nếu gặp lại tình huống tương tự, em sẽ nêu rủi ro sớm hơn và chuẩn bị phương án giảm phạm vi cụ thể. Em cũng nói rõ phần nào là bằng chứng, phần nào chỉ là giả thuyết, để người quyết định hiểu đúng mức chắc chắn.
""", [("Nếu đây chỉ là tình huống giả định thì trả lời thế nào?", "Mở đầu bằng 'Nếu gặp tình huống này, em sẽ…' và mô tả hành động dự kiến. Không kể theo quá khứ như một kinh nghiệm đã xảy ra.")], "Nêu rủi ro có căn cứ; không biến mọi bất đồng thành lý do dừng release.", kind="experience", minutes=4)

add("design-withdrawal", "System design • 40 phút", "Thiết kế rút tiền từ ví về ngân hàng", "Requirements → invariants → estimation → API/data → flow → failures → operations", """
Em sẽ đi từ yêu cầu và những điều kiện phải luôn đúng, sau đó ước tính tải, thiết kế API và dữ liệu, rồi kiểm tra các tình huống lỗi. Em muốn thống nhất rằng phạm vi là rút tiền từ ví về tài khoản ngân hàng đã xác minh; việc liên kết tài khoản, KYC và chống gian lận có thể là dependency với hợp đồng rõ ràng.

Trước khi vẽ, em muốn hỏi: người dùng cần kết quả cuối ngay hay chấp nhận pending? Có bao nhiêu giao dịch mỗi ngày và peak TPS? Ngân hàng hỗ trợ mã tham chiếu chống trùng, inquiry và callback như thế nào? Có yêu cầu hạn mức, currency, đối soát và thời gian xử lý ngoại lệ không? Nếu chưa có số liệu, em xin dùng giả định dưới đây để thiết kế và sẽ điều chỉnh khi có thông tin.

Em chốt ba invariant: không chi vượt số dư khả dụng; một ý định rút tiền không tạo tác động tiền nhiều lần; mọi thay đổi tiền và trạng thái đều truy vết được. Em bổ sung rằng timeout không đủ để kết luận thất bại. Khi chưa biết kết quả ngân hàng, hệ thống phải giữ trạng thái có thể xác minh lại thay vì tự release tiền.

Em giả định 1 triệu giao dịch một ngày, trung bình khoảng 11,6 giao dịch mỗi giây, peak gấp 20 là khoảng 232 TPS. Nếu mỗi giao dịch phát sinh 5 lần đọc trạng thái, tải đọc trung bình khoảng 58 RPS và peak cần ước tính riêng theo hành vi client. Mỗi giao dịch cùng metadata ở mức 2 KB sẽ khoảng 2 GB mỗi ngày, khoảng 730 GB một năm trước index, replicas, ledger và audit. Với 232 request mỗi giây và thời gian chờ ngân hàng trung bình 2 giây trong một trạng thái tải ổn định tương ứng, số lời gọi đang xử lý khoảng 464; đây là kiểm tra capacity, không phải kết luận tạo 464 thread là đủ.

Ở high-level, API xác thực và nhận yêu cầu, Transfer module điều phối state machine, Wallet/Ledger quản lý tiền và BankConnector xử lý giao thức đối tác. Database quan hệ giữ nguồn sự thật; outbox và worker đưa công việc ra ngoài transaction ngắn. Callback receiver và inquiry worker đưa kết quả về cùng logic transition. Reconciliation so sánh với dữ liệu ngân hàng; notification là nhánh tách rời. Để giữ thiết kế ban đầu đơn giản, em có thể để Transfer và Wallet/Ledger chung một database transaction; nếu tách service sở hữu dữ liệu riêng thì cần giao thức hold idempotent và recovery tương ứng.

API tạo yêu cầu là POST /v1/withdrawals, có Idempotency-Key, bankAccountId, amount và currency. User ID lấy từ credential đã xác minh, không tin userId tùy ý trong body. Hệ thống kiểm tra tài khoản đích thuộc người dùng, quyền, hạn mức và dữ liệu. Khi yêu cầu được nhận bền vững nhưng chưa hoàn tất, em trả 202 cùng transactionId, status và link tra cứu. GET /v1/withdrawals/{id} cũng kiểm tra ownership. Cùng key nhưng khác payload trả lỗi xung đột; cùng key và cùng payload trả về giao dịch hiện có theo hợp đồng.

Em lưu wallet với available, held và version; withdrawal với owner, amount, currency, bank reference, status và version; idempotency record với scope, key và request fingerprint; cùng ledger, outbox và callback inbox. Unique constraint trên phạm vi key và định danh từng tác động bảo vệ race. Ledger entry có account, debit/credit, currency và business reference; mỗi journal phải cân bằng theo currency. Các bảng hold và số dư là mô hình phục vụ quyết định, được cập nhật cùng nguồn sự thật trong transaction đã chọn. Em không dựa vào chỉ một enum để bảo đảm tiền đúng.

Luồng chính bắt đầu bằng claim idempotency key. Trong cùng transaction, em cập nhật có điều kiện để giảm available, tăng held nếu đủ tiền, tạo withdrawal và outbox. Nếu không đủ thì không commit một giao dịch đã giữ tiền. Nếu database báo kết quả commit chưa rõ do lỗi kết nối, request tiếp theo tra cứu qua cùng key để xác minh, không tạo key mới. Sau commit, relay phát công việc; worker claim việc rồi gọi ngân hàng bằng bank reference ổn định, không giữ row lock qua lời gọi mạng.

State machine đơn giản có HELD, SUBMITTED, PENDING_CONFIRMATION, SUCCEEDED và FAILED_CONFIRMED. HELD chỉ xuất hiện sau khi hold đã commit. SUBMITTED biểu diễn đã bắt đầu gửi hoặc đang theo dõi bước gửi, không chứng minh ngân hàng đã nhận. Chỉ bằng chứng kết quả chắc chắn mới đưa sang terminal. Transition được bảo vệ bằng version hoặc điều kiện trên trạng thái hiện tại, với bút toán và outbox kết quả trong cùng transaction. Nếu trạng thái và ledger tách DB, em phải thay phần nguyên tử này bằng protocol rõ ràng, không bỏ qua khoảng hở.

Khi ngân hàng thành công, em chốt hold và ledger đúng một lần. Nếu ngân hàng xác nhận thất bại cuối cùng, em release hold đúng một lần. Nếu timeout, connection reset hoặc process chết sau khi gửi, em không biết lệnh đã thực hiện chưa. Worker phục hồi sẽ inquiry theo bank reference hoặc retry cùng định danh nếu ngân hàng có idempotency đáng tin. Nếu đối tác không hỗ trợ cả hai đủ tốt, em cần quy trình đối soát và xử lý ngoại lệ; không thể hứa exactly-once bằng một Kafka topic.

Callback được kiểm tra chữ ký, freshness theo giao thức, reference, amount và currency. Em lưu receipt bền vững trước khi xác nhận nhận thành công với đối tác, hoặc xử lý nguyên tử theo hợp đồng. Callback trùng bị dedupe; callback đến trước response vẫn được áp dụng nếu transition hợp lệ. Callback cũ không được hạ SUCCEEDED về PENDING. Nếu ngân hàng gửi hai kết quả terminal mâu thuẫn, em không dùng last-write-wins mà đưa vào điều tra/đối soát và giữ audit evidence.

Outbox relay có thể phát trùng, consumer có thể chết sau DB commit trước ack. Vì thế các tác động có business key duy nhất và consumer ghi nhận xử lý nguyên tử với dữ liệu của mình. Việc dedupe message không đủ cho tác động ngân hàng ngoài transaction, nên bank reference phải đi xuyên suốt. Em test riêng các crash window này. Một lease worker hết hạn không chứng minh worker cũ đã dừng; fencing/version và đối tác idempotency phải ngăn tác động xấu khi có hai worker.

Về lỗi dependency, em giới hạn concurrency và pool theo ngân hàng, timeout từng lời gọi và deadline tổng. Retry có backoff, jitter và ngân sách; một tầng chịu trách nhiệm retry để tránh nhân tải. Breaker giúp fail-fast hoặc hoãn công việc mới khi ngân hàng lỗi, nhưng các giao dịch chưa rõ vẫn được xác minh có kiểm soát. Client thấy trạng thái đang xử lý và được hướng dẫn tra cứu; không được lặp việc trả tiền chỉ vì notification chưa tới.

Đối soát so sánh bank reference, amount, currency và trạng thái giữa ledger/withdrawal với báo cáo hoặc inquiry của ngân hàng. Em xét cutoff, timezone, file completeness và settlement delay để không kết luận lệch quá sớm. Các loại lệch gồm bên mình có bên ngân hàng không có, ngược lại, sai số tiền và khác trạng thái. Hệ thống tạo case có ownership, SLA xử lý và phê duyệt khi cần adjustment. Không chỉnh dữ liệu cho khớp mà mất dấu vết.

Về scale, API và worker có thể scale ngang nhưng database, account nóng và giới hạn ngân hàng mới là những điểm cần đo. Em thêm index theo owner và thời gian cho lịch sử, theo trạng thái/next check cho inquiry, và retention/archive cho dữ liệu cũ. Cache phù hợp với cấu hình, không là căn cứ cuối cho số dư. Nếu cần shard theo wallet, giao dịch liên shard là một bài toán bổ sung; em chưa thêm độ phức tạp đó khi tải giả định chưa chứng minh cần.

Vận hành cần success rate theo ngân hàng, p95/p99, số và tuổi giao dịch pending, held quá lâu, outbox lag, duplicate callbacks và lệch đối soát. Correlation ID nối API, worker và callback; log che dữ liệu nhạy cảm. Em phân biệt SLO nhận yêu cầu bền vững với SLO hoàn tất tiền, đồng thời chốt RPO/RTO và khả năng failover trước khi hứa không mất dữ liệu. Khi không xác lập được quyền ghi nhất quán, thao tác chi tiền cần dừng hoặc pending, không ghi ở hai nơi độc lập.

Cuối bài, lựa chọn của em là transaction ngắn trong vùng sở hữu tiền, workflow bất đồng bộ có định danh ổn định, idempotency nhiều lớp và đối soát. Đánh đổi là một số giao dịch chờ lâu hơn khi đối tác không rõ kết quả, nhưng em có cách bảo vệ tiền và phục hồi có kiểm soát. Em sẵn sàng đi sâu vào schema, cơ chế hold hoặc một crash window cụ thể theo phần anh muốn kiểm tra.
""", [
("Nếu giữ tiền lâu, user khó chịu thì sao?", "Thiết kế pending SLA, inquiry có ngân sách, cảnh báo và xử lý ngoại lệ. Chính sách release phải có căn cứ về kết quả và phân bổ rủi ro được phê duyệt; không suy ra timeout nghĩa là ngân hàng chưa trả tiền."),
("Nếu không dùng message broker?", "Worker có thể đọc durable work/outbox trong DB với claim/version đúng. Broker là lựa chọn phân phối tải; cần chứng minh độ bền và recovery, không bắt buộc Kafka để thiết kế hợp lệ."),
("Nếu ngân hàng không có idempotency?", "Giảm gửi lại tự động, dùng inquiry/reference nếu được hỗ trợ, đối soát và manual resolution. Nêu giới hạn bảo đảm; không giả định hệ thống mình kiểm soát được side effect ở đối tác."),
("Nếu wallet và transfer nằm ở hai database?", "Tạo protocol Reserve/Confirm/Release idempotent với operation ID, lưu state từng phía và recovery. Không còn local ACID cho cả hai; cần giải thích timeout ở từng bước và ownership của hold.")
], "Các con số là giả định luyện tập, không phải traffic hoặc kiến trúc nội bộ của Zalopay.", kind="design", minutes=40,
extra="""
<h4>Chạy bài 40 phút: nói, vẽ và tự trả lời</h4>
<table><thead><tr><th>Mốc</th><th>Việc cần hoàn thành</th></tr></thead><tbody>
<tr><td>0–4 phút</td><td>Đọc mở bài, hỏi requirements, chốt scope và 3 invariants.</td></tr>
<tr><td>4–7 phút</td><td>Tính TPS, storage và in-flight calls trên giấy. Nói rõ giả định và overhead chưa tính.</td></tr>
<tr><td>7–13 phút</td><td>Vẽ kiến trúc, đánh dấu source of truth, đồng bộ/bất đồng bộ và boundary database.</td></tr>
<tr><td>13–21 phút</td><td>Viết API, schema, unique constraints; vẽ state machine và happy path.</td></tr>
<tr><td>21–31 phút</td><td>Tự trả lời lần lượt: timeout, callback trước response, callback trùng, worker crash, DB commit chưa rõ.</td></tr>
<tr><td>31–37 phút</td><td>Giải thích đối soát, bottleneck, metric, failover và bảo mật.</td></tr>
<tr><td>37–40 phút</td><td>Nêu trade-offs, trả lời 1–2 câu hỏi sâu và chốt giới hạn bảo đảm.</td></tr>
</tbody></table>
<p>Script lời nói khoảng 15–20 phút tùy nhịp. Thời gian còn lại dành cho vẽ, tính toán và câu hỏi đào sâu; không cố kéo dài bằng cách đọc chậm.</p>
<h4>Sơ đồ để tập vẽ</h4>
<pre>Client → API / Auth → Transfer + Wallet/Ledger → SQL database
                         │                         │
                         │                    Outbox (cùng TX)
                         │                         ↓
                         │                   Relay → Queue
                         │                         ↓
                         │                   Bank worker → Bank
                         │                                    │
                         └── Transition handler ← Callback ───┘
                                  ↑
                           Inquiry / Reconciliation
                                  │
                             Result outbox → Notifications</pre>
<h4>Schema tối thiểu để giải thích trên bảng</h4>
<pre>wallet(id, owner_id, currency, available_minor, held_minor, version)
withdrawal(id, wallet_id, bank_account_ref, amount_minor, currency,
           status, bank_reference UNIQUE, version, next_check_at)
idempotency(scope, key, fingerprint, withdrawal_id, created_at)
  UNIQUE(scope, key)
journal(id, business_reference UNIQUE, currency, created_at)
ledger_entry(id, journal_id, account_id, side, amount_minor)
outbox(event_id PRIMARY KEY, aggregate_id, event_type, payload, status)
callback_inbox(bank_id, event_key, payload_hash, received_at, status)
  UNIQUE(bank_id, event_key)</pre>
<p>Currency và đơn vị nhỏ nhất phải được định nghĩa. Journal cân bằng cần được enforce bằng logic transaction/constraint phù hợp; chỉ tạo các cột không tự bảo đảm điều đó. Nếu ngân hàng không có event ID, thiết kế khóa dedupe theo hợp đồng và vẫn bảo vệ business transition.</p>
<h4>Cập nhật giữ tiền: đoạn minh họa</h4>
<pre>BEGIN;
-- Claim idempotency key bằng unique constraint, xử lý conflict rõ ràng.
UPDATE wallet
SET available_minor = available_minor - :amount,
    held_minor = held_minor + :amount,
    version = version + 1
WHERE id = :wallet_id
  AND currency = :currency
  AND available_minor &gt;= :amount;
-- amount phải &gt; 0; yêu cầu đúng 1 row updated.
-- Tạo withdrawal, reservation/audit và outbox cùng transaction.
COMMIT;
-- HTTP tới ngân hàng thực hiện sau transaction này.</pre>
<h4>State machine</h4>
<pre>HELD → SUBMITTED → SUCCEEDED
              ├→ FAILED_CONFIRMED
              └→ PENDING_CONFIRMATION → SUCCEEDED / FAILED_CONFIRMED
Callback có thể tới trước response: kiểm tra bằng chứng + transition,
không ép phải nhận response API trước mới chấp nhận kết quả.</pre>
""")

add("design-variants", "System design • Mở rộng", "Payment Gateway, Wallet, Loyalty và Notification", "Giữ framework • thay invariant và nguồn sự thật theo bài toán", """
Nếu đề là Payment Gateway, em làm rõ merchant tạo payment intent, ngân hàng hoặc PSP xử lý tiền, còn gateway sở hữu trạng thái điều phối và webhook. Em không tự giả định gateway giữ số dư ví. Em tách một intent với các attempt, giữ định danh chống trùng và không tạo attempt mới ở ngân hàng khác khi attempt cũ vẫn có thể thành công. Webhook merchant dùng event ID ổn định, chữ ký, retry có giới hạn và API tra cứu; webhook lỗi không làm payment thành công chạy lại.

Nếu đề là eWallet, em mở rộng bài rút tiền sang nạp và chuyển nội bộ. Em làm rõ ledger là nguồn sự thật nào, available/held được tính hoặc materialize ra sao, và một journal phải cân bằng theo currency. Chuyển nội bộ trong cùng database có thể ghi debit và credit nguyên tử; tách shard hoặc owner service thì cần protocol và recovery mới. 100K concurrent users phải được đổi thành workload bằng giả định hành vi, không xem là 100K TPS. Event sourcing là lựa chọn có đánh đổi, không mặc định bắt buộc.

Nếu đề là Loyalty, invariant là không redeem vượt điểm khả dụng và mỗi sự kiện earn chỉ tạo điểm một lần. Em lưu point lots có ngày hết hạn, rule/campaign version và business event ID. Redeem phân bổ theo quy tắc như hết hạn sớm trước và phải atomic với cập nhật lot; expiry job có thể chạy lại an toàn. Eventual consistency phù hợp với hiển thị hoặc ghi nhận earn có độ trễ, nhưng quyết định redeem cần bảo vệ cạnh tranh với redeem khác và expiry. Em không sửa rule cũ rồi để replay tính ra điểm khác mà không có policy.

Nếu đề là Notification, em tách event nghiệp vụ với delivery job theo channel, template version, recipient và locale. Worker theo email/SMS/push có quota, retry, provider timeout và DLQ. Em phân biệt provider accepted với người dùng thực sự nhận; timeout sau khi provider nhận có thể gây duplicate nếu retry và provider không hỗ trợ idempotency. Dedupe trong DB không tự xóa khoảng hở đó. Fanout lớn dùng batch/cursor và backpressure, ưu tiên thông báo giao dịch so với marketing theo policy.

Ở cả bốn bài, em vẫn bắt đầu từ requirements, estimation và invariants, rồi chọn source of truth và vẽ failure path. Em chỉ dùng lại pattern khi giả định tương thích; không sao chép nguyên wallet schema cho mọi sản phẩm. Đánh đổi được nói rõ ở chỗ cần consistency mạnh, chỗ chấp nhận trễ và khả năng phục hồi khi dependency không có bảo đảm mình mong muốn.
""", [("Luyện bài phụ thế nào?", "Chọn một đề, dành 3 phút requirements/invariants, 3 phút estimation, 6 phút API/data/flow và 8 phút failure/trade-off. Dùng đoạn script tương ứng làm mở bài, rồi tự vẽ và trả lời checklist bên dưới.")], "Đây là script chuyển đề và checklist mở rộng, không phải bốn bản đọc 40 phút độc lập.", kind="design", minutes=20, priority=False,
extra="""<h4>Checklist để tự mở rộng từng đề</h4><ul>
<li><strong>Gateway:</strong> merchant auth; intent/attempt; bank reference; callback và webhook tách biệt; settlement/reconciliation; merchant portal tra cứu.</li>
<li><strong>Wallet:</strong> ledger accounts; journal cân bằng; hold/confirm/release; chuyển nội bộ; cross-shard; audit và adjustment.</li>
<li><strong>Loyalty:</strong> earn dedupe; rule version; lot expiry; redeem đồng thời; refund điểm; campaign timezone; replay.</li>
<li><strong>Notification:</strong> template version; preferences theo loại thông báo; fanout; rate limit provider; accepted/delivered; PII retention; duplicate window.</li>
</ul><h4>Bài phụ Rate Limiter — 20 phút</h4><p>Dùng script Token Bucket trong nhóm Giao dịch: dành 4 phút chốt scope và burst; 5 phút mô tả state token/timestamp và phép refill; 5 phút atomic Redis update, TTL, cluster/hot key; 6 phút Redis failover, fail-open/closed, fallback và metric. Viết phép refill = min(capacity, tokens + elapsed × rate), rồi chỉ trừ token nếu đủ chi phí request.</p>""")
