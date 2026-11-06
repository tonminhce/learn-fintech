"""Build a portable, dependency-free HTML study guide from authored content."""
from pathlib import Path
import html
import runpy

ROOT = Path(__file__).resolve().parents[1]
CARDS = runpy.run_path(str(ROOT / "content" / "guide.py"))["CARDS"]
SOURCES = {
    "java-concurrency": ("Oracle · Java 8 concurrency & happens-before", "https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/package-summary.html"),
    "future": ("Oracle · CompletableFuture (Java 8)", "https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CompletableFuture.html"),
    "virtual": ("Oracle · Virtual threads (Java 21)", "https://docs.oracle.com/en/java/javase/21/core/virtual-threads.html"),
    "gc": ("Oracle · G1 và lựa chọn garbage collector", "https://docs.oracle.com/en/java/javase/21/gctuning/garbage-first-g1-garbage-collector1.html"),
    "spring-tx": ("Spring · Declarative transactions", "https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html"),
    "spring-security": ("Spring Security · Servlet architecture", "https://docs.spring.io/spring-security/reference/servlet/architecture.html"),
    "mysql": ("MySQL 8.4 · InnoDB isolation levels", "https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html"),
    "kafka": ("Apache Kafka · Delivery semantics", "https://kafka.apache.org/41/design/design/"),
    "oauth": ("IETF · RFC 9700, OAuth2 security", "https://www.rfc-editor.org/rfc/rfc9700.html"),
    "oidc": ("OpenID Foundation · OpenID Connect Core", "https://openid.net/specs/openid-connect-core-1_0.html"),
    "jwt": ("IETF · RFC 8725, JWT best practices", "https://www.rfc-editor.org/rfc/rfc8725.html"),
    "saml": ("OASIS · SAML 2.0 technical overview", "https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html"),
    "tls": ("IETF · RFC 8446, TLS 1.3", "https://www.rfc-editor.org/rfc/rfc8446.html"),
    "pci-sad": ("PCI SSC · Sensitive authentication data after authorization", "https://www.pcisecuritystandards.org/faqs/for-pci-dss-why-is-storage-of-sensitive-authentication-data-sad-after-authorization-not-permitted-even-when-there-are-no-primary-account-numbers-pans-in-an-environment/"),
    "pci-pan": ("PCI SSC · Protecting cardholder data", "https://blog.pcisecuritystandards.org/protecting-cardholder-data-with-encryption"),
    "redis": ("Redis · Rate limiting", "https://redis.io/docs/latest/develop/use-cases/rate-limiter/"),
}


def esc(value):
    return html.escape(str(value), quote=True)


def paragraphs(text):
    return "\n".join(f"<p>{esc(p)}</p>" for p in text.split("\n\n") if p.strip())


def card_html(card, index):
    kind_labels = {"theory": "Lý thuyết", "experience": "Kinh nghiệm", "design": "System design"}
    structure = {"theory": "Khái niệm → Cơ chế → Ví dụ → Trade-off", "experience": "Bối cảnh → Trách nhiệm → Lựa chọn → Bằng chứng → Bài học", "design": "Yêu cầu → Invariants → Ước tính → API & dữ liệu → Luồng → Lỗi → Vận hành"}
    cid = esc(card["id"])
    script = paragraphs(card["script"])
    questions = "".join(f'<div class="follow"><h4>{esc(q)}</h4><p>{esc(a)}</p></div>' for q, a in card["follow"])
    refs = " · ".join(f'<a href="{esc(SOURCES[r][1])}" target="_blank" rel="noopener noreferrer">{esc(SOURCES[r][0])}</a>' for r in card["refs"])
    badge = '<span class="badge priority">Ưu tiên cao</span>' if card["priority"] else '<span class="badge">Mở rộng</span>'
    note_label = "Câu chuyện thật của Minh · điền các chỗ [ngoặc vuông]" if card["kind"] == "experience" else "Ghi chú của Minh"
    warning = '<div class="personal">Mẫu kể chuyện, không phải kinh nghiệm có sẵn. Điền dữ kiện thật và luyện cùng phần ghi chú bên dưới.</div>' if card["kind"] == "experience" else ""
    return f'''<article class="card" id="{cid}" data-group="{esc(card['group'])}" data-priority="{str(card['priority']).lower()}" data-kind="{card['kind']}">
    <div class="card-meta"><span class="number">{index:02d}</span><span>{kind_labels[card['kind']]}</span><span>·</span><span>{'35–40' if card['minutes']==40 else ('1–2' if card['kind']=='theory' else ('3–5' if card['kind']=='experience' else card['minutes']))} phút</span>{badge}</div>
    <h3><a class="permalink" href="#{cid}">{esc(card['title'])}</a></h3>
    <p class="cue">{esc(card['cue'])}</p>
    <div class="card-actions"><button class="read-toggle" aria-expanded="true" aria-controls="answer-{cid}">Ẩn script</button><button class="done-toggle" aria-pressed="false">Đánh dấu đã luyện</button><button class="save-toggle" aria-pressed="false" aria-label="Lưu câu: {esc(card['title'])}">Lưu câu</button><button class="start-timer" data-minutes="{card['minutes']}">◷ {card['minutes']} phút</button></div>
    <div class="answer" id="answer-{cid}"><div class="structure">{structure[card['kind']]}</div>{warning}<div class="spoken">{script}</div>
    {('<details class="workbench"><summary>Bảng vẽ & hướng dẫn thực hành</summary>'+card['extra']+'</details>') if card['extra'] else ''}
    <details class="deep-dive"><summary>Manager hỏi tiếp · {len(card['follow'])} câu</summary>{questions}</details>
    <div class="trap"><strong>Điểm dễ mất điểm</strong><p>{esc(card['trap'])}</p></div>
    {('<p class="card-sources">Đọc gốc: '+refs+'</p>') if refs else ''}</div>
    <details class="notes"><summary>{note_label}</summary><label for="note-{cid}">Chỉ lưu trong trình duyệt này. Không gửi lên GitHub.</label><textarea id="note-{cid}" data-note="{cid}" rows="5" placeholder="Ví dụ thật, con số đã kiểm chứng, điều muốn hỏi thêm…"></textarea></details>
    </article>'''


groups = list(dict.fromkeys(c["group"] for c in CARDS))
nav = ''.join(f'<button class="nav-item" data-category="{esc(g)}"><span>{esc(g)}</span><span>{sum(c["group"]==g for c in CARDS):02d}</span></button>' for g in groups)
cards = '\n'.join(card_html(c, i) for i, c in enumerate(CARDS, 1))
sources = ''.join(f'<li><a href="{esc(url)}" target="_blank" rel="noopener noreferrer">{esc(title)} ↗</a></li>' for title, url in SOURCES.values())
css = (ROOT / 'styles.css').read_text(encoding='utf-8')
js = (ROOT / 'app.js').read_text(encoding='utf-8')
theory_count = sum(c['kind'] == 'theory' for c in CARDS)
html_page = f'''<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark"><meta name="description" content="Sổ tay luyện nói phỏng vấn Bank Solutions: Java, Spring, OOP, bảo mật và system design. Script tiếng Việt, mở offline, không cần đăng nhập.">
<title>Fintech Fieldnotes — Sổ tay phỏng vấn của Minh</title><style>{css}</style></head>
<body><a class="skip" href="#library">Đến nội dung</a>
<aside class="sidebar"><a class="brand" href="#top"><span class="brand-mark">f.</span><span>fintech<span class="brand-sub">FIELDNOTES / VOL. 01</span></span></a>
<div class="sidebar-intro">SỔ TAY CỦA MINH<span>Hiểu sâu. Nói rõ.</span></div>
<details class="nav-wrap" open><summary>Chọn chủ đề <span>⌄</span></summary><nav aria-label="Chủ đề"><button class="nav-item active" data-category="all" aria-pressed="true"><span>Tất cả bài luyện</span><span>{len(CARDS)}</span></button>{nav}</nav></details>
<div class="progress-box"><div><span>Nhịp luyện của bạn</span><strong id="progress-label">0/{len(CARDS)}</strong></div><progress id="progress" max="{len(CARDS)}" value="0" aria-label="Số bài đã luyện"></progress><p>Không cần thuộc từng chữ.<br>Hãy kể lại bằng cách của mình.</p></div>
<a class="sources-nav" href="#references">Tài liệu gốc ↗</a><div class="sidebar-bottom">BANK SOLUTIONS<br>INTERVIEW PRACTICE · 2026</div></aside>
<main id="top"><header class="topbar"><span>LEARN / FINTECH ENGINEERING</span><div><button id="theme" aria-label="Chuyển sang giao diện tối">Giao diện tối</button><a href="https://github.com/tonminhce/learn-fintech" target="_blank" rel="noopener noreferrer">GitHub ↗</a></div></header>
<section class="hero"><div><p class="eyebrow"><span></span> CHUẨN BỊ CHO BUỔI PHỎNG VẤN 2 GIỜ</p><h1>Hiểu bản chất.<br><em>Nói thành lời.</em></h1><p class="hero-copy">Bộ script để Minh đọc thành tiếng, luyện cách lập luận và tự tin đi sâu vào từng quyết định kỹ thuật.</p><div class="hero-actions"><button class="primary" id="start-priority">Bắt đầu với câu ưu tiên <span>↗</span></button><button id="open-design" class="secondary">Luyện system design →</button></div><p class="hero-foot">Java · OOP · Spring · Distributed systems · Security</p></div>
<div class="hero-note"><div class="note-top">BUỔI LUYỆN HÔM NAY <span>01 / 03</span></div><h2>Đừng học thuộc.<br> Hãy giải thích.</h2><ol><li><span>01</span><div><strong>Đọc để quen mồm</strong><p>Nắm mạch lập luận và ví dụ.</p></div></li><li><span>02</span><div><strong>Ẩn script, tự trả lời</strong><p>Bấm giờ, nói bằng lời của mình.</p></div></li><li><span>03</span><div><strong>Hỏi thêm “nếu lỗi thì sao?”</strong><p>Thử một race condition hoặc timeout.</p></div></li></ol><div class="note-bottom">MỘT CÂU TRẢ LỜI TỐT CÓ CẢ GIỚI HẠN.</div></div></section>
<section class="stats" aria-label="Nội dung"><div><strong>{theory_count:02d}</strong><span>script lý thuyết<br>1–2 phút / câu</span></div><div><strong>05</strong><span>mẫu kể kinh nghiệm<br>3–5 phút / câu</span></div><div><strong>40<span>′</span></strong><span>bài thiết kế chính<br>kèm API, schema & lỗi</span></div><div><strong>∞</strong><span>lượt luyện lại<br>offline, không đăng nhập</span></div></section>
<section class="howto"><strong>Trước khi bắt đầu</strong><p>Câu ưu tiên được chọn từ JD và gợi ý HR, không phải đề nội bộ hay cam kết xác suất được hỏi. Đọc script lý thuyết theo nhịp tự nhiên; thời lượng là mục tiêu luyện. Kinh nghiệm có [chỗ trống] cần điền sự thật. Bài 40 phút gồm cả vẽ, tính toán và câu hỏi đào sâu.</p></section>
<section id="library" class="library"><div class="section-heading"><div><p class="eyebrow">YOUR PRACTICE LIBRARY</p><h2 id="section-title">Tất cả bài luyện</h2></div><span id="result-count" role="status" aria-live="polite">{len(CARDS)} bài</span></div>
<div class="toolbar"><label class="search"><span aria-hidden="true">⌕</span><input id="search" type="search" placeholder="Tìm câu hỏi, ví dụ: volatile, timeout, SSO…" aria-label="Tìm trong câu hỏi và script"></label><div class="tools"><label class="sr-only" for="filter">Lọc bài luyện</label><select id="filter"><option value="all">Tất cả trạng thái</option><option value="priority">Ưu tiên cao</option><option value="saved">Đã lưu</option><option value="todo">Chưa luyện</option><option value="done">Đã luyện</option></select><button id="practice" aria-pressed="false">Ẩn tất cả script</button><button id="font-down" aria-label="Giảm cỡ chữ">A−</button><button id="font-up" aria-label="Tăng cỡ chữ">A+</button><button id="print">In phần đang lọc</button></div></div>
<noscript><p class="notice">JavaScript đang tắt. Bạn vẫn đọc và in được toàn bộ script; tìm kiếm, bộ đếm giờ và lưu tiến độ cần JavaScript.</p></noscript>
<p id="storage-warning" class="notice" hidden>Trình duyệt không cho lưu cục bộ. Bạn vẫn đọc và luyện được, nhưng tiến độ/ghi chú có thể mất khi đóng trang.</p>
<div id="cards">{cards}</div><div id="empty" hidden><h3>Chưa tìm thấy bài phù hợp.</h3><p>Thử một từ khóa ngắn hơn hoặc xóa bộ lọc.</p><button id="clear-filters" class="primary">Xóa tìm kiếm & bộ lọc</button></div></section>
<section id="references" class="references"><p class="eyebrow">READ THE ORIGINALS</p><h2>Tài liệu để đi sâu hơn.</h2><p>Script là nội dung luyện tập biên soạn riêng. Các nguồn chính thức dưới đây dùng để đối chiếu cơ chế; luôn xem đúng phiên bản Java, Spring và database của hệ thống thực tế. Không có dữ liệu riêng hay kiến trúc nội bộ của Zalopay trong tài liệu.</p><ul>{sources}</ul></section>
<footer><span>FINTECH FIELDNOTES · VIẾT ĐỂ LUYỆN NÓI</span><p>Nội dung cập nhật 06.11.2026 · Ghi chú & tiến độ chỉ lưu trên trình duyệt đang dùng. Không nhập thông tin mật của công ty hoặc khách hàng vào ghi chú luyện tập.</p><a href="#top">Về đầu trang ↑</a></footer></main>
<div id="timer" class="timer" hidden role="region" aria-label="Đồng hồ luyện nói"><div><span id="timer-label">Đang luyện</span><strong id="timer-display" role="timer">02:00</strong></div><button id="timer-pause">Tạm dừng</button><button id="timer-reset">Làm lại</button><button id="timer-close" aria-label="Đóng bộ đếm giờ">×</button></div><div id="announcement" class="sr-only" role="status" aria-live="polite"></div>
<script>{js}</script></body></html>'''
html_page = '\n'.join(line.rstrip() for line in html_page.splitlines()) + '\n'
(ROOT / 'index.html').write_text(html_page, encoding='utf-8')
print(f'Built index.html: {len(CARDS)} cards; {theory_count} theory, 5 experience, 2 design; {len(html_page):,} characters.')
